import os
import sys
import logging
import numpy as np
import pandas as pd
import re
from datetime import datetime
import time
import utils

LOG_LEVEL = "INFO"
try:
    if( (os.environ["LOG_LEVEL"]=="INFO") or (os.environ["LOG_LEVEL"]=="DEBUG") ):
        LOG_LEVEL = os.environ["LOG_LEVEL"]
except:
    pass
logging.basicConfig(stream=sys.stdout,
                    format='%(levelname)s: '\
                           '%(asctime)s:' \
                           '%(module)s:' \
                           '%(funcName)s:' \
                           '%(lineno)s: ' \
                           '%(message)s')
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

abs_dir_path_processor = '/Users/scottquincey/Desktop/21-22/final-year-project/experimental_results/processor'
abs_dir_path_processed_data = '/Users/scottquincey/Desktop/21-22/final-year-project/experimental_results/processed_data'
abs_dir_path_archive = '/Users/scottquincey/Desktop/21-22/final-year-project/experimental_results/archive_of_original_files'

all_files_in_directory = [d for d in os.listdir(abs_dir_path_processor)]

print(all_files_in_directory)

for current_file in all_files_in_directory:

    lines_in_file = utils.read_data_from_txt_file_and_insert_commas(logger, abs_dir_path_processor, current_file)

    utils.cut_original_file_into_archive_folder(logger, abs_dir_path_processor, abs_dir_path_archive, current_file)

    processed_folder_name = utils.make_processed_folder_for_new_processed_data(logger, abs_dir_path_processor, abs_dir_path_processed_data, current_file)

    utils.write_new_data_txt_file_in_new_folder(lines_in_file, abs_dir_path_processed_data, processed_folder_name)

    utils.copy_txt_data_file_to_csv_file_in_new_folder(logger, abs_dir_path_processed_data, processed_folder_name)

    utils.create_config_file(logger, abs_dir_path_processed_data, processed_folder_name, lines_in_file)

    time.sleep(1) #To make sure files don't have the same names







