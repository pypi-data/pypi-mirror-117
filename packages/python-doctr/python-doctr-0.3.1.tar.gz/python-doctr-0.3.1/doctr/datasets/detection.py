# Copyright (C) 2021, Mindee.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

import os
import json
import numpy as np
from typing import List, Tuple, Dict, Any, Optional, Callable

from .datasets import AbstractDataset
from doctr.utils.geometry import fit_rbbox

__all__ = ["DetectionDataset"]


class DetectionDataset(AbstractDataset):
    """Implements a text detection dataset

    Example::
        >>> from doctr.datasets import DetectionDataset
        >>> train_set = DetectionDataset(img_folder=True, label_folder="/path/to/label_folder")
        >>> img, target = train_set[0]

    Args:
        img_folder: folder with all the images of the dataset
        label_folder: folder with all the corresponding labels (stem needs to be identical)
        sample_transforms: composable transformations that will be applied to each image
        rotated_bbox: whether polygons should be considered as rotated bounding box (instead of straight ones)
    """
    def __init__(
        self,
        img_folder: str,
        label_folder: str,
        sample_transforms: Optional[Callable[[Any], Any]] = None,
        rotated_bbox: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(img_folder, **kwargs)
        self.sample_transforms = sample_transforms

        self.data: List[Tuple[str, Dict[str, Any]]] = []
        np_dtype = np.float16 if self.fp16 else np.float32
        for img_path in os.listdir(self.root):
            # File existence check
            if not os.path.exists(os.path.join(self.root, img_path)):
                raise FileNotFoundError(f"unable to locate {os.path.join(self.root, img_path)}")
            with open(os.path.join(label_folder, img_path + '.json'), 'rb') as f:
                boxes = json.load(f)
            bboxes = np.asarray(boxes["boxes_1"] + boxes["boxes_2"] + boxes["boxes_3"], dtype=np_dtype)
            if rotated_bbox:
                # Switch to rotated rects
                bboxes = np.asarray([list(fit_rbbox(box)) for box in bboxes], dtype=np_dtype)
            else:
                # Switch to xmin, ymin, xmax, ymax
                bboxes = np.concatenate((bboxes.min(axis=1), bboxes.max(axis=1)), axis=1)

            is_ambiguous = [False] * (len(boxes["boxes_1"]) + len(boxes["boxes_2"])) + [True] * len(boxes["boxes_3"])
            self.data.append((img_path, dict(boxes=bboxes, flags=np.asarray(is_ambiguous))))

    def __getitem__(
        self,
        index: int
    ) -> Tuple[Any, Dict[str, np.ndarray]]:

        img, target = self._read_sample(index)
        h, w = self._get_img_shape(img)
        if self.sample_transforms is not None:
            img = self.sample_transforms(img)

        # Boxes
        boxes = target['boxes'].copy()
        boxes[..., [0, 2]] /= w
        boxes[..., [1, 3]] /= h

        return img, dict(boxes=boxes.clip(0, 1), flags=target['flags'])
