import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
_base_ = [
    'my_model/deeplabv3_unet/my_datasets.py',
    'my_model/deeplabv3_unet/deeplabv3_unet_s5-d16.py',
    'configs/_base_/default_runtime.py',
    'configs/_base_/schedules/schedule_40k.py'
]
model = dict(test_cfg=dict(crop_size=(128, 128), stride=(85, 85),num_class=3))
evaluation = dict(metric='mDice')
