import os
import glob
import xml.etree.ElementTree as ET
import shutil
import pathlib

import numpy as np
from tqdm import tqdm
#import cv2
from PIL import ImageDraw, Image

def crop_and_paste(cxcy_list, wh_list, background, original_img):
    ## destruct
    cx, cy = cxcy_list
    w, h = wh_list
    ## get start point
    start_x = 0
    start_y = 0
    #print(h, w)
    #print(cy, cx)
    ## crop the image
    cropped_img = original_img[start_y:start_y+h, start_x:start_x+w]
    #print(cropped_img.shape)
    ## assert the cropping
    assert cropped_img.shape[0] == h
    assert cropped_img.shape[1] == w
    ## paste to white background by unpacking each channel
    #for i in range(3):
    background[start_y:start_y+h, start_x:start_x+w, :] = cropped_img 
    #print(background.shape)
    return background

def purify(img_dir, dst):
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
    #bin_pat = np.random.randint(low=0, high=1, size=len(img_file_list))
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
        ## generate a white background
        img_background = np.ones((height, width, 3)) * 255
        #print(width, height)
        for obj in root.findall('object'):
            bndbox_anno = obj.find('robndbox')
            #print(bndbox_anno)
            wh_list = [bndbox_anno.find(tag).text for tag in ['w', 'h']]
            wh_list = np.array(wh_list, dtype=np.float).astype(np.int)
            ## get padding dims wrt to bbox h w
            #pad_w, pad_h = get_pad_size(wh_list, bin_pat[idx])
            cxcy_list = [int(bndbox_anno.find(tag).text) for tag in ['cx', 'cy']]
            angle = int(np.degrees(float(bndbox_anno.find('angle').text)))
            ## if 90 or 270 swap the list
            if angle in [90, 270]:
                wh_list[0], wh_list[1] = wh_list[1], wh_list[0]

            new_img = crop_and_paste(cxcy_list, wh_list, img_background, img)
            #print(new_img.shape)
            img_pil = Image.fromarray(np.uint8(new_img))
            img_pil.save(pathlib.PurePath(dst, img_file.split('/')[-1]).as_posix())
            #cx, cy = cxcy_list
            #new_cxcy = [cx + pad_w, cy + pad_h]
            #new_width_height = [width + pad_w * 2, height + pad_h * 2]
            ## write the new values
            #for idx, t in enumerate(['cx', 'cy']):
            #    bndbox_anno.find(t).text = str(new_cxcy[idx])
            
            #root.find('size').find('width').text = str(new_width_height[0])
            #root.find('size').find('height').text = str(new_width_height[1])

purify('../train_single_0_90_180_270_bordered_corrected', '../debug_data')