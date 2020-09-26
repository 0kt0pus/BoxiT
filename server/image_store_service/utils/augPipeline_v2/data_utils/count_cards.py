from pure_utils import *
import os
import numpy as np
import xml.etree.ElementTree as ET
import functools

def count_objects(img_dir, labels):
    #obj_dict = {k: v for k, v in zip(labels,
    #                                 [0 for _ in range(len(labels))])}
    #print(obj_dict)
    ## Object dict gives you all paths for each object
    obj_path_dict = dict()
    obj_count_dict = dict()
    img_path_list = get_img_paths(img_dir)
    
    for img_path in img_path_list:
        #print(img_path)
        xfile = '.'.join([os.path.splitext(img_path)[0], 'xml'])
        xml_keys = ET.parse(xfile)
        root = xml_keys.getroot()

        for obj in root.findall('object'):
            name = obj.find('name').text
            obj_path_dict.setdefault(name, []).append(img_path)

    ## count all the objects per class
    for k, v in obj_path_dict.items():
        obj_count_dict[k] = len(v)
    #print(obj_count_dict)
    ## give report
    total = list()
    print()
    for lb in labels:
        v = obj_count_dict.get(lb)
        total.append(v)
        print("{}: {}".format(lb, v))
    total_num_data = functools.reduce(lambda x, y: x+y, total)
    print()
    print("TOtal number of images: {}".format(total_num_data))
    print()
    return obj_path_dict, obj_count_dict

    #print(obj_path_dict[labels[31]])
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
count_objects('../noBorder_Testing_modeA/', labels)
'''