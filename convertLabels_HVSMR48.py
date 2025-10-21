import multiprocessing
import shutil
from multiprocessing import Pool

import SimpleITK as sitk
import numpy as np
from batchgenerators.utilities.file_and_folder_operations import *
from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


def copy_segmentation_and_convert_labels_to_nnUNet(in_file: str, out_file: str) -> None:
    # use this for segmentation only!!!
    # nnUNet wants the labels to be continuous. BraTS is 0, 1, 2, 4 -> we make that into 0, 1, 2, 3
    img = sitk.ReadImage(in_file)
    img_npy = sitk.GetArrayFromImage(img)

    uniques = np.unique(img_npy)
    print(uniques)
    for u in uniques:
        if u not in [0, 203, 204, 205, 206, 207, 208, 209, 210]:
            raise RuntimeError('unexpected label')

    # relabel = {0:0, 201:0, 202:0, 203:1, 204:2, 205:3, 206:4, 207:5, 208:6, 209:7, 210:8} <-- from Danielle
    # label_ids = ['bg', 'aorta', 'lv', 'pa', 'ra', 'svc', 'ivc', 'la', 'rv']
    seg_new = np.zeros_like(img_npy)
    seg_new[img_npy == 210] = 8
    seg_new[img_npy == 209] = 7
    seg_new[img_npy == 208] = 6
    seg_new[img_npy == 207] = 5
    seg_new[img_npy == 206] = 4
    seg_new[img_npy == 205] = 3
    seg_new[img_npy == 204] = 2
    seg_new[img_npy == 203] = 1
    seg_new[img_npy == 202] = 0
    seg_new[img_npy == 201] = 0
    img_corr = sitk.GetImageFromArray(seg_new)
    img_corr.CopyInformation(img)
    sitk.WriteImage(img_corr, out_file)

init_folder = "sixty_subjects"
dataset_folder = "Dataset606_HVSMR48_raw"
if __name__ == '__main__':
    
    folder_path = f"/mnt/datastore/jubair/datasets/{init_folder}/labels"
    dest_path = f"{nnUNet_raw}/{dataset_folder}/labelsTr"
    
    for count, filename in enumerate(sorted(os.listdir(folder_path))):
        src = f"{folder_path}/{filename}"
        dst = f"{dest_path}/{filename}"
        copy_segmentation_and_convert_labels_to_nnUNet(src, dst)
    
    folder_path_img = f"/mnt/datastore/jubair/datasets/{init_folder}/images"
    dest_path_img = f"{nnUNet_raw}/{dataset_folder}/imagesTr"
    
    for count, filename in enumerate(sorted(os.listdir(folder_path_img))):
        src = f"{folder_path_img}/{filename}"
        dst = f"{dest_path_img}/{filename}"
        shutil.copy(src, dst)