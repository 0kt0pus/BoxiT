import os
import pathlib
from utils import *
import xml.etree.ElementTree as ET
import data_utils.pure_utils as pu

import numpy as np
from PIL import Image

## current labels
'''
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
'''
req_card_types = ['AT', 'BC', 'PA', 'FSPI']
req_sides = ['A', 'B']
req_angles = ['0', '20', '40', '60', '80', '90', '100', '120', '140', '160', '180', '200', '220', '240', '260', '270', '280', '300', '320', '340']
labels = ['_'.join([c_ty, c_sd, c_ag]) 
                            for c_ty in req_card_types
                                for c_sd in req_sides
                                    for c_ag in req_angles]
## Potential extensions, xml should be first
EXT_LIST = ['jpg', 'png', 'jpeg']
#data_dir = '/Users/melukadesilva/Documents/Research_assistant_work/uniquare/phase_4_progress/data/val'
## Load a dataset with pascalvoc annotations, 
## the image and annotation name must be similar
class PascalVocDataLoader:
    def __init__(self, data_dir):
        ## load the data paths
        ## get the existing valid image paths
        valid_exts = get_valid_exts(data_dir, EXT_LIST)
        ## get the corresponding images, as a list of list where
        ## the 0th dim is the extension and 1st dim the file list
        img_path_list = [get_ext_paths(data_dir, ext) for ext in valid_exts]
        ## flat the list of list to a list
        self.img_path_list = flatten(img_path_list)
    def __len__(self):
        return len(self.img_path_list)
    def __getitem__(self, idx):
        img_path = self.img_path_list[idx]
        xml_path = '.'.join([os.path.splitext(img_path)[0], 'xml'])
        #print(xml_path)
        ## load the image
        img_pil = Image.open(img_path)
        img = np.array(img_pil)
        ## parse the xml tree
        tree = ET.parse(xml_path)
        root = tree.getroot()
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        #print(width, height)
        ## hold the bboxes and catagory id
        bbox_list = list()
        for obj in root.findall('object'):
            name = obj.find('name')
            bndbox_anno = obj.find('robndbox')
            ## for the moment data is on cxcywha format
            cxcywha_list = [float(bndbox_anno.find(tag).text) for tag in ['cx', 'cy', 'w', 'h', 'angle']]
            ## get the square box
            cxcywh_list = pu.rot2square(cxcywha_list)
            ## get extream coordinates (required by augmenter)
            bbox_list.append(pu.tlbr(cxcywh_list))
            ## append the category for the augmenter
            bbox_list.append([labels.index(name.text)])

        return (img, bbox_list, img_path, cxcywh_list)

'''
d_loader = PascalVocDataLoader(data_dir)
print(d_loader.__getitem__(1))
'''