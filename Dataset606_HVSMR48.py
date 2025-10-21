import multiprocessing
import shutil
from multiprocessing import Pool

import SimpleITK as sitk
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


foldername = 'Dataset606_HVSMR48_raw'
output_folder=join(nnUNet_raw, foldername)
regions_class_order = None
channel_names={0: 'CT'}

folder_path = join(output_folder, 'imagesTr')
for count, filename in enumerate(sorted(os.listdir(folder_path))):
    continue
# print(count)

labels={
            "background": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8  
        }
num_training_cases=count+1
file_ending='.nii.gz'
    

generate_dataset_json(output_folder,
                    channel_names,
                    labels,
                    num_training_cases,
                    file_ending,
                    regions_class_order
                    )