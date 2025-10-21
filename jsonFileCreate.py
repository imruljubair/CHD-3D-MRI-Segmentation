import os
import sys
import json
from nnunetv2.paths import nnUNet_raw

datasetname = "Dataset606_HVSMR48_raw"

test_files = []
test_folder_path  = f"{nnUNet_raw}/{datasetname}/imagesTs/"
for count, filename in enumerate(sorted(os.listdir(test_folder_path))):
# count = 3
    # dst = f"{folder_path}pat{str(count).zfill(2)}.nii.gz"
    fname = f"{test_folder_path}{filename}"
    test_files.append(fname)
# print(test_files)
test_count = len(test_files)


train_files = []
val_files = []
train_folder_path  = f"{nnUNet_raw}/{datasetname}/imagesTr/"
train_label_folder_path  = f"{nnUNet_raw}/{datasetname}/labelsTr/"

for count, filename in enumerate(sorted(os.listdir(train_label_folder_path))):
# count = 3
    # dst = f"{folder_path}pat{str(count).zfill(2)}.nii.gz"
    if count%5==0:
        fname_label = f"{train_label_folder_path}{filename}"
        fname_im = f"{train_folder_path}HVSMR_" + str(count).zfill(3) + "_0000.nii.gz"
        temp_dict = {
            "image": fname_im,
            "label": fname_label
        }
        val_files.append(temp_dict)
    else:
        fname_label = f"{train_label_folder_path}{filename}"
        fname_im = f"{train_folder_path}HVSMR_" + str(count).zfill(3) + "_0000.nii.gz"
        temp_dict = {
            "image": fname_im,
            "label": fname_label
        }
        train_files.append(temp_dict)

# print(train_files)

# Data to be written
dictionary = {
    "description": "HVSMR48",
    "labels": {
        "0": "bg",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8"
    },
    "licence": "yt",
    "modality": {
        "0": "MRI"
    },
    "name": "btcv",
    "numTest": len(test_files),
    "numTraining": len(train_files),
    "reference": "Vanderbilt University",
    "release": "1.0 06/08/2015",
    "tensorImageSize": "3D",
    "test": test_files,
    "training": train_files,
    "validation": val_files
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json

with open("/mnt/datastore/jubair/datasets/For_swin_Unetr/data/dataset_0.json", "w") as outfile:
    outfile.write(json_object)