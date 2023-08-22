import logging.config
import os
import json

LOGGING_CONFIG_FILE = 'logging.json'
LOGGER_NAME = 'myapp'
script_directory = os.path.dirname(os.path.abspath(__file__))
SRC_DIRECTORY = os.path.dirname(script_directory)
PROJECT_DIR = os.path.dirname(SRC_DIRECTORY)
DATA_DIR = os.path.join(PROJECT_DIR,'data')
RAW_DATA_DIR = os.path.join(DATA_DIR,'raw')

def _build_logging_config_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(PROJECT_DIR,'config', LOGGING_CONFIG_FILE)
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

print(PROJECT_DIR)
