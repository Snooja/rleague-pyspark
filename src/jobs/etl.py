# ------- Only required to run file directly for syntax checking
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir))
# -------

from shared.utils import PROJECT_DIR, RAW_DATA_DIR, logger
import zipfile
ZIPFILE_NAME = 'archive.zip'
import os

# Extract from zipfile
def _build_zipfile_path():
    p = os.path.join(RAW_DATA_DIR,ZIPFILE_NAME)
    return p

def extract_data(destination_dir:str = RAW_DATA_DIR):
    zip_file_path = _build_zipfile_path()
    destination_dir = os.path.join(destination_dir)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(destination_dir)
        logger.info(f"raw data extacted to {destination_dir}")

if __name__ == "__main__":
    extract_data()


