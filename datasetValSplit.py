import os
import sys
import json
from nnunetv2.paths import nnUNet_raw

def main():
    
    datasetname = "Dataset606_HVSMR48_raw"
    
    fold_A =   ["pat00.nii.gz",
                "pat05.nii.gz",
                "pat12.nii.gz",
                "pat16.nii.gz",
                "pat23.nii.gz",
                "pat24.nii.gz",
                "pat26.nii.gz",
                "pat27.nii.gz",
                "pat37.nii.gz",
                "pat42.nii.gz",
                "pat46.nii.gz",
                "pat54.nii.gz"]
    
    fold_B =   ["pat02.nii.gz",
                "pat03.nii.gz",
                "pat06.nii.gz",
                "pat08.nii.gz",
                "pat09.nii.gz",
                "pat14.nii.gz",
                "pat19.nii.gz",
                "pat34.nii.gz",
                "pat45.nii.gz",
                "pat48.nii.gz",
                "pat53.nii.gz",
                "pat59.nii.gz"]
    
    fold_C =   ["pat11.nii.gz",
                "pat13.nii.gz",
                "pat15.nii.gz",
                "pat18.nii.gz",
                "pat22.nii.gz",
                "pat25.nii.gz",
                "pat31.nii.gz",
                "pat36.nii.gz",
                "pat44.nii.gz",
                "pat55.nii.gz",
                "pat56.nii.gz",
                "pat58.nii.gz"]
    
    fold_D =   ["pat01.nii.gz",
                "pat04.nii.gz",
                "pat07.nii.gz",
                "pat10.nii.gz",
                "pat17.nii.gz",
                "pat30.nii.gz",
                "pat33.nii.gz",
                "pat35.nii.gz",
                "pat38.nii.gz",
                "pat40.nii.gz",
                "pat51.nii.gz",
                "pat52.nii.gz"]

    all_folds = {"fold_A": fold_A,
                 "fold_B": fold_B,
                 "fold_C": fold_C,
                 "fold_D": fold_D}
    
    # print(len(all_folds))
    # all_folds_for_json = {
    #                     "train": [],
    #                     "val":[]
    #                     }
    all_folds_for_json = []
    for fold_id, fold_items in all_folds.items():
        folder_path = f"{nnUNet_raw}/{datasetname}/imagesTr"
        # print(folder_path)
        tr_ = []
        vl_ = []
        for count, filename in enumerate(sorted(os.listdir(folder_path))):
            a = f"HVSMR_" + str(count).zfill(3)       
            if filename in fold_items:
                vl_.append(a)
            else:
                tr_.append(a)
            temp_dict = {
                        "train": tr_,
                        "val":vl_
                        } 
        all_folds_for_json.append(temp_dict)   
        
    # print(all_folds_for_json)
    json_object = json.dumps(all_folds_for_json, indent=4)
 
# Writing to sample.json

    with open(f"/mnt/datastore/jubair/codes/nnUnet/{datasetname}_splits_final.json", "w") as outfile:
        outfile.write(json_object)
    
    folder_path = f"{nnUNet_raw}/{datasetname}/imagesTr"
    for count, filename in enumerate(sorted(os.listdir(folder_path))):
        dst = f"HVSMR_" + str(count).zfill(3) + "_0000.nii.gz"
        src = f"{folder_path}/{filename}"
        dst = f"{folder_path}/{dst}"
        
        os.rename(src, dst)
    
    folder_path = f"{nnUNet_raw}/{datasetname}/imagesTs"    
    for count, filename in enumerate(sorted(os.listdir(folder_path))):
        dst = f"HVSMR_" + str(count).zfill(3) + "_0000.nii.gz"
        src = f"{folder_path}/{filename}"
        dst = f"{folder_path}/{dst}"
        
        os.rename(src, dst)   
 
    
    folder_path = f"{nnUNet_raw}/{datasetname}/labelsTr" 
    for count, filename in enumerate(sorted(os.listdir(folder_path))):
        dst = f"HVSMR_" + str(count).zfill(3) + ".nii.gz"
        src = f"{folder_path}/{filename}"
        dst = f"{folder_path}/{dst}"
        
        os.rename(src, dst)          
        
    folder_path = f"{nnUNet_raw}/{datasetname}/labelsTs" 
    for count, filename in enumerate(sorted(os.listdir(folder_path))):
        dst = f"HVSMR_" + str(count).zfill(3) + ".nii.gz"
        src = f"{folder_path}/{filename}"
        dst = f"{folder_path}/{dst}"
        
        os.rename(src, dst) 
       
if __name__ == '__main__':
    main()