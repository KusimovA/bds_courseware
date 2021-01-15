from bds_courseware import read_drive_dataset, pandas_read_drive_csv
from bds_courseware import print_dataset_description

d = {
    "cwur": ("19Q0suXlfLuWrklmhx_hvQeOAnKC5GOEe", "csv"),
    "edu_expenditure": ("1_srtnVijt6R8SZKMY4pNb_VMbfc-2DAd", "csv"),
    "edu_attainment": ("1W9PKdqYHLVz_z0nKJOB-w1crJvCHOBky", "csv"),
    "school_and_country": ("1erNL48vR68e1794kHPGP4GRpA-ZlJ5At", "csv"),
    "shanghai": ("1kCF2EJuOyfUAOkQBmUdo39ZLKCgx2RyH", "csv"),
    "times": ("1tDf8pJTCHhdcLsnCvDnefX-q1oz1tVLQ", "csv"),
    "bank_full": ("1mCPUi9nHDHAfHGYf0oi-tnhbkCGTb_Mg", "ssv"),
    "bank_prep_full": ("15hKFhmB71WwTdqNF5_29TPsqW5PyGa50", "csv.gz"),
}
for i in d.keys():
    print(i)
    df = get_dataset(i)
    print(df.shape)

df = get_stock_data("BAJAJ-AUTO")
print(df.shape)
