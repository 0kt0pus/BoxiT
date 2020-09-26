import os
import glob
import xml.etree.ElementTree as ET
import shutil
import pathlib

import numpy as np
from tqdm import tqdm
from blend_img import *
#import cv2
from PIL import ImageDraw, Image

def get_pad_size(wh_list, bin_id):
    w, h = wh_list
    # if 0 height major and if 1 width major
    if bin_id == 0:
        ## 50% of height and 25% of width
        pad_h = (h)
        pad_w = (w // 2)
    if bin_id == 1:
        ## 25% of height and 50% of width
        pad_h = (h // 2)
        pad_w = (w)

    return pad_w, pad_h

def append_border(img_dir, dst):
    print(img_dir)
    def filter_xmls(elem):
        if elem.split('/')[-1].split('.')[-1] == 'xml' or \
           elem.split('/')[-1].split('.')[-1] == 'py' or \
            elem.split('/')[-1].split('.')[-1] == 'json':
            return False
        else:
            return True
    ## get all xmls
    #img_dir='../data/Cards_Balanced_Dataset_v2'
    #print(img_dir)
    is_train = False if img_dir.split('/')[-1] == 'val' else True
    print(is_train)
    xml_paths = glob.glob(os.path.join(img_dir, '*.xml'))
    ## get all paths
    file_list = list()
    for root, subdir, files in os.walk(img_dir):
        for name in files:
            file_path = pathlib.PurePath(img_dir, name)
            file_list.append(file_path.as_posix())
    img_file_list = list(filter(filter_xmls, file_list))
    ## binary pattern to decide if width major or height major
    bin_pat = np.random.randint(low=0, high=1, size=len(img_file_list))
    #print(bin_pat)
    #for i in img_file_list:
    #print(img_file_list)
    #    print(i)
    for idx, img_file in enumerate(tqdm(img_file_list)):
        ## open img
        img_pil = Image.open(img_file)
        img = np.array(img_pil)
        #print(img.shape)
        #print(img)
        #h = img.shape[0]
        #w = img.shape[1]
        #print(h, w)

        xfile = pathlib.PosixPath(img_dir, '.'.join((img_file.split('/')[-1].split('.')[0], 'xml')))
        xml_keys = ET.parse(xfile)
        root = xml_keys.getroot()
        
        width = int(root.find('size').find('width').text)
        height = int(root.find('size').find('height').text)
        #print(width, height)
        for obj in root.findall('object'):
            bndbox_anno = obj.find('robndbox')
            #print(bndbox_anno)
            wh_list = [bndbox_anno.find(tag).text for tag in ['w', 'h']]
            wh_list = np.array(wh_list, dtype=np.float).astype(np.int)
            ## get padding dims wrt to bbox h w
            pad_w, pad_h = get_pad_size(wh_list, bin_pat[idx])
            cxcy_list = [int(bndbox_anno.find(tag).text) for tag in ['cx', 'cy']]
            cx, cy = cxcy_list
            new_cxcy = [cx + pad_w, cy + pad_h]
            new_width_height = [width + pad_w * 2, height + pad_h * 2]
            ## write the new values
            for idx, t in enumerate(['cx', 'cy']):
                bndbox_anno.find(t).text = str(new_cxcy[idx])
            
            root.find('size').find('width').text = str(new_width_height[0])
            root.find('size').find('height').text = str(new_width_height[1])

        '''
        #print(pad_w, pad_h)
        for obj in xml_keys.find('object'):
            bndbox_anno = obj.find('robndbox')
            print(bndbox_anno)
            cxcy_list = [bndbox_anno.find(tag).text for tag in ['cx', 'cy']]
            cx, cy = cxcy_list
            new_cxcy = [cx + pad_w, cy + pad_h]
            ## write the new values
            for idx, t in enumerate(['cx', 'cy']):
                bndbox_anno.find(t).text = new_cxcy[idx]
        '''
        
        #ET.tostring(root)
        #print(root)
        
        xml_keys.write(pathlib.PurePath(dst, xfile.as_posix().split('/')[-1]).as_posix())
        
        ## pad the image with the compute w h
        img_new = list()
        for i in range(3):
            img_new.append(np.pad(img[:, :, i], ((pad_h, pad_h),(pad_w, pad_w)), 'constant', constant_values=((255, 255), (255, 255))))
        img = np.stack(img_new)
        #print(img.shape)
        img = np.transpose(img, (1, 2, 0))
        #print(img.shape)
        #print(img.shape)
        #h = img.shape[0]
        #w = img.shape[1]
        #print(h, w)
        #print()
        ## save the new image at dst
        ## copy first the xmls
        #shutil.copyfile(xfile, pathlib.PurePath(dst, xfile.as_posix().split('/')[-1]).as_posix())
        ## save the image
        
        img_pil = Image.fromarray(img)
        img_pil.save(pathlib.PurePath(dst, img_file.split('/')[-1]).as_posix())
        


append_border(os.path.abspath('../val'), os.path.abspath('../debug_data'))