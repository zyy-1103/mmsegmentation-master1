# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset
@DATASETS.register_module()
class MyDataset(CustomDataset):
    CLASSES = ('opticCup', 'opticDisk','background')
    PALETTE = [[0,0,0], [128, 128, 128],[255,255,255]]
    def __init__(self, **kwargs):
        super(MyDataset, self).__init__(
            **kwargs)