import os
import pathlib
import shutil
from tqdm import tqdm
from pure_utils import *
'''
def filter_xmls(elem):
    if elem.split('/')[-1].split('.')[-1] == 'xml' or \
        elem.split('/')[-1].split('.')[-1] == 'py' or \
        elem.split('/')[-1].split('.')[-1] == 'json':
        return False
    else:
        return True

## get all paths
file_list = list()
for root, subdir, files in os.walk(img_dir):
    for name in files:
        #print(root)
        #print(name)
        file_path = pathlib.PurePath(root, name)
        file_list.append(file_path.as_posix())
img_file_list = list(filter(filter_xmls, file_list))
'''
def move_files(img_dir, dst_dir):
    img_file_list = get_img_paths(img_dir)
    #print(img_file_list)
    ##mv files
    for img_file in tqdm(img_file_list):
        src_img_file = img_file
        #print(src_img_file)
        src_xfile = '.'.join([os.path.splitext(img_file)[0], 'xml'])
        #print(xfile)
        #print(img_file)
        dst_img_file = pathlib.PurePath(dst_dir, os.path.split(src_img_file)[-1]).as_posix()
        dst_xfile = pathlib.PurePath(dst_dir, os.path.split(src_xfile)[-1]).as_posix()
        ## copy the files
        shutil.copyfile(src_img_file, dst_img_file)
        shutil.copyfile(src_xfile, dst_xfile)


#img_dir = '../train_single_0_90_180_270_bordered_augmented_3_rgb_temp'
#dst_dir = '../train_single_0_90_180_270_bordered_augmented_3_rgb'
    