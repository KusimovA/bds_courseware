from bds_courseware import read_drive_dataset
from bds_courseware import print_dataset_description, print_module_datasets
from bds_courseware import DATASETS

print("Dataset names: ", DATASETS.keys())
name = "breastw"
df = read_drive_dataset(*DATASETS[name])
print(df.head(2))
print(df.shape)
