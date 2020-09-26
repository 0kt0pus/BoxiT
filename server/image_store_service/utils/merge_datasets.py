import os
import pathlib
import shutil
from pure_utils import *
from count_cards import count_objects
import numpy as np
from tqdm import tqdm

## take a subset of images and merge it with a primary dataset
def merge_data(primary_dir, subset_dir, labels, subset_size):
    #img_path_primary_list = get_img_paths(primary_dir)
    img_path_subset, img_count_subset = count_objects(subset_dir, labels)
    ## get a subset of images for merging
    img_selected_path_dict = dict()
    for k, v in img_path_subset.items():
        img_selected_path_dict[k] = v[:subset_size] if subset_size < len(v) else v
    #print(len(img_selected_path_dict[labels[0]]))
    ## get the src path and set the dst path
    for k, v in tqdm(img_selected_path_dict.items()):
        for img_path in v:
            #print(path)
            #print(len(v))
            dst_img_path = pathlib.PurePath(
                primary_dir, img_path.split('/')[-1]
            ).as_posix()
            src_xml_path = '.'.join([os.path.splitext(img_path)[0], 'xml'])
            dst_xml_path = '.'.join([os.path.splitext(dst_img_path)[0], 'xml'])
            #print(src_xml_path)
            #print(dst_img_path)
            #print(dst_xml_path)
            shutil.copyfile(img_path, dst_img_path)
            shutil.copyfile(src_xml_path, dst_xml_path)


labels = [
    'AT_A_0',
    'AT_A_90',
    'AT_A_180',
    'AT_A_270',
    'AT_B_0',
    'AT_B_90',
    'AT_B_180',
    'AT_B_270',
    'PA_A_0',
    'PA_A_90',
    'PA_A_180',
    'PA_A_270',
    'PA_B_0',
    'PA_B_90',
    'PA_B_180',
    'PA_B_270',
    'BC_A_0',
    'BC_A_90',
    'BC_A_180',
    'BC_A_270',
    'BC_B_0',
    'BC_B_90',
    'BC_B_180',
    'BC_B_270',
    'FSPI_A_0',
    'FSPI_A_90',
    'FSPI_A_180',
    'FSPI_A_270',
    'FSPI_B_0',
    'FSPI_B_90',
    'FSPI_B_180',
    'FSPI_B_270',
]
merge_data('../val_mode_A_B/', '../noBorder_Testing_modeA/', labels, 8)
