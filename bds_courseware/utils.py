import pandas as pd
from bds_courseware.const import DATASETS


def print_dataset_description(dataset_name):
    pass


def read_drive_dataset(file_id, data_type="csv"):
    if data_type == "tsv":
        return pandas_read_drive_csv(file_id, sep="\t")
    if data_type == "tsv.gz":
        return pandas_read_drive_csv(file_id, sep="\t", compression="gzip")
    if data_type == "csv":
        return pandas_read_drive_csv(file_id)
    if data_type == "csv.gz":
        return pandas_read_drive_csv(file_id, compression="gzip")
    if data_type == "ssv":
        return pandas_read_drive_csv(file_id, sep=";")
    if data_type == "ssv.gz":
        return pandas_read_drive_csv(file_id, sep=";", compression="gzip")


def pandas_read_drive_csv(file_id, **read_csv_args):
    download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
    try:
        return pd.read_csv(download_link, **read_csv_args)
    except pd.errors.ParserError:
        raise IOError("Data source is not shared to everyone, check access rights on Google Drive")


def get_stock_data(name):
    """
    Fetch stock data by company `name`
    """
    from ._ids import _stock_parts

    if name in _stock_parts:
        return read_drive_data(_stock_parts[name])
    else:
        raise IndexError(f"Uknown company name. {name} was given.")


def get_dataset(name):
    """
    Fetch dataset by `name`
    """
    from ._ids import _datasets

    if name in _datasets:
        return read_drive_data(*_datasets[name])
    else:
        raise IndexError(
            f"Uknown company name. {name} was given. Available datasets are {_datasets.keys()}"
        )
