import logging.config
import os
import json
from kaggle.api import dataset_download_files

LOGGING_CONFIG_FILE = 'logging.json'
LOGGER_NAME = 'myapp'

def _build_logging_config_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, '..','..','config', LOGGING_CONFIG_FILE)
    return (config_file_path)

def setup_logger():
    config_file_path = _build_logging_config_file_path()

    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
        logging.config.dictConfig(config)
    
    logger = logging.getLogger(LOGGER_NAME)
    logger.info(f"succesfully setup logger using {config_file_path}")
    return logger

# Initialize the logger when the module is imported
logger = setup_logger()

#TBC
def download_data(
        dataset_url = 
):
    dataset_download_files(
        dataset = ,
        path = ,
        force = false,
        unzip = True
    )
