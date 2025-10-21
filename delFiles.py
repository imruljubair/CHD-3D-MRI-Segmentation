import glob, os

foldername="Dataset606_HVSMR48_raw"
for f in glob.glob(f"/mnt/datastore/jubair/datasets/For_nnUnet/nnUNet_raw/{foldername}/imagesTr/*.nii.gz"):
    os.remove(f)
    

for f in glob.glob(f"/mnt/datastore/jubair/datasets/For_nnUnet/nnUNet_raw/{foldername}/imagesTs/*.nii.gz"):
    os.remove(f)
    

for f in glob.glob(f"/mnt/datastore/jubair/datasets/For_nnUnet/nnUNet_raw/{foldername}/labelsTr/*.nii.gz"):
    os.remove(f)
    

for f in glob.glob(f"/mnt/datastore/jubair/datasets/For_nnUnet/nnUNet_raw/{foldername}/labelsTs/*.nii.gz"):
    os.remove(f)