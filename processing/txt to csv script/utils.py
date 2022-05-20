import os
import sys
import logging
import numpy as np
import pandas as pd
import re
from datetime import datetime


def read_data_from_txt_file_and_insert_commas(logger, 
                                              abs_dir_path_processor, 
                                              current_file):

    logger.info("Reading data from %s", current_file)
    
    lines_in_file = []

    data_file = open(os.path.join(abs_dir_path_processor, current_file), 'r')

    line = data_file.readline()
    line = line.replace('\t', ',')

    while line != '':
        lines_in_file.append(line)
        line = data_file.readline()
        line = line.replace('\t', ',')

    data_file.close()

    logger.info("Data from %s read and tabs replaced with commas", current_file)

    return lines_in_file


def cut_original_file_into_archive_folder(logger, 
                                          abs_dir_path_processor, 
                                          abs_dir_path_archive, 
                                          current_file):

    basename = os.path.basename(os.path.join(abs_dir_path_processor, 
                                             current_file))
    os.rename(os.path.join(abs_dir_path_processor, 
                           current_file), os.path.join(abs_dir_path_archive, 
                                                       basename))

    logger.info("%s cut into archive folder", current_file)


def make_processed_folder_for_new_processed_data(logger, 
                                                 abs_dir_path_processor, 
                                                 abs_dir_path_processed_data, 
                                                 current_file):
    now = datetime.now()
    date_time = now.strftime(" %d/%m/%Y/%H-%M-%S")
    date_time = date_time.replace('/', '_')

    basename = os.path.basename(os.path.join(abs_dir_path_processor, 
                                             current_file))
    basename = basename.replace(' ', '_')

    processed_folder_name = basename + date_time
    
    os.makedirs(os.path.join(abs_dir_path_processed_data, 
                             processed_folder_name))

    logger.info("Folder %s has been created at %s", processed_folder_name,\
                                os.path.join(abs_dir_path_processed_data, 
                                             processed_folder_name))

    return processed_folder_name


def write_new_data_txt_file_in_new_folder(lines_in_file, 
                                          abs_dir_path_processed_data, 
                                          processed_folder_name):
    used_lines = lines_in_file[1:]
    
    new_text_file = open(os.path.join(abs_dir_path_processed_data, 
                                      processed_folder_name, 
                                      processed_folder_name + '.txt'), 'w')

    for x in used_lines:
        new_text_file.write(x)

    new_text_file.close()

def copy_txt_data_file_to_csv_file_in_new_folder(logger, 
                                                 abs_dir_path_processed_data, 
                                                 processed_folder_name):

    read_file = pd.read_csv (os.path.join(abs_dir_path_processed_data, 
                                          processed_folder_name, 
                                          processed_folder_name + '.txt'))
    read_file.to_csv (os.path.join(abs_dir_path_processed_data, 
                                   processed_folder_name, 
                                   processed_folder_name + '.csv'), index=None)
    logger.info("CSV file created in %s",\
                                 os.path.join(abs_dir_path_processed_data, 
                                              processed_folder_name, 
                                              processed_folder_name + '.csv'))


def create_config_file(logger, 
                       abs_dir_path_processed_data, 
                       processed_folder_name, 
                       lines_in_file):
    config_file = open(os.path.join(abs_dir_path_processed_data, 
                                    processed_folder_name, 'config.txt'), 'w')
    config_file.write(lines_in_file[0])
    config_file.close()
    logger.info("Configuration file has been added to %s. Data for Thickness"+
                "and Current Channel Width can be found here.",\
                os.path.join(abs_dir_path_processed_data, 
                             processed_folder_name))









