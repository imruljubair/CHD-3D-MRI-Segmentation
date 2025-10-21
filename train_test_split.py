import os
import sys
import shutil
from nnunetv2.paths import nnUNet_raw
from tqdm import tqdm


def main():
    
    datasetname = "Dataset606_HVSMR48_raw"
    # foldername = "imagesTs"
    # foldername = "imagesTr"

    from_folder_path = f"{nnUNet_raw}/{datasetname}/imagesTr"
    to_folder_path = f"{nnUNet_raw}/{datasetname}/imagesTs"
    
    from_folder_path_label = f"{nnUNet_raw}/{datasetname}/labelsTr"
    to_folder_path_label = f"{nnUNet_raw}/{datasetname}/labelsTs"

    test_files = ["pat21.nii.gz",
                  "pat28.nii.gz", 
                  "pat29.nii.gz",
                  "pat32.nii.gz",
                  "pat39.nii.gz",
                  "pat41.nii.gz",
                  "pat43.nii.gz",
                  "pat47.nii.gz",
                  "pat49.nii.gz",
                  "pat50.nii.gz", 
                  "pat57.nii.gz",
                  "pat60.nii.gz"]
    
    for _, filename in enumerate(sorted(os.listdir(from_folder_path))):

        if filename in test_files:
            src = f"{from_folder_path}/{filename}"
            dst = f"{to_folder_path}/{filename}"
            print(f"test file {filename} moved")
            # print(filename)
            shutil.move(src, dst)        
     
    for _, filename in enumerate(sorted(os.listdir(from_folder_path_label))):

        if filename in test_files:       
            src = f"{from_folder_path_label}/{filename}"
            dst = f"{to_folder_path_label}/{filename}"
            print(f"test label file {filename} moved")
            shutil.move(src, dst)     
        
        
if __name__ == '__main__':
    main()