import os
import sys
from nnunetv2.paths import nnUNet_raw

def main():
    
    datasetname = "Dataset606_HVSMR48_raw"

    # foldername = "imagesTr"
    # foldername = "imagesTs"
    # foldername = "labelsTr"
    foldername = "labelsTs"


    
    # folder_path = int(sys.argv[1])
    # folder_path = "/mnt/datastore/jubair/datasets/For_nnUnet/nnUNet_raw/Dataset101_CHDMRI_Soroosh/imagesTr"
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