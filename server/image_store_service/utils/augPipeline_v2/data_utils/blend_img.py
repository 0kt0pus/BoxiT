import numpy as np
import os
import glob
import xml.etree.ElementTree as ET
import shutil
import pathlib

import cv2
import numpy as np
from tqdm import tqdm
#import cv2
from PIL import ImageDraw, Image

def get_backgrounds(fn_get_path, src, num_bg_req):
    background_file_list = fn_get_path(src)
    num_bgs = len(background_file_list)
    ## generate a random pattern size equal to num_bg_req
    draw_pattern = np.random.randint(low=0, high=num_bgs-1, size=num_bg_req)
    bg_pack = list()
    for bg_idx in draw_pattern:
        bg_pack.append(background_file_list[bg_idx])
    
    return bg_pack

def get_img_paths(img_dir: str) -> list:
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
    ## get all paths
    file_list = list()
    for root, subdir, files in os.walk(img_dir):
        for name in files:
            file_path = pathlib.PurePath(root, name)
            file_list.append(file_path.as_posix())
    img_file_list = list(filter(filter_xmls, file_list))

    return img_file_list

def crop(wh_list, original_img):
    ## destruct
    w, h = wh_list
    ## get start point
    start_x = 0#cx - w // 2
    start_y = 0#cy - h // 2
    #print(h, w)
    #print(cy, cx)
    ## crop the image
    cropped_img = original_img[start_y:start_y+h, start_x:start_x+w]
    #print(cropped_img.shape)
    ## assert the cropping
    assert cropped_img.shape[0] == h
    assert cropped_img.shape[1] == w
    
    return cropped_img

def blend_imgs(src1, src2, dst, content_wh):
    # src1 foreground
    # src2 background
    ## get the img path list
    img_file_list = get_img_paths(src1)
    bg_for_blend_list = get_backgrounds(get_img_paths, src2, len(img_file_list))
    #print(len(bg_for_blend))
    #print(len(img_file_list))
    
    for idx, (img_file, bg_file) in tqdm(enumerate(zip(img_file_list, bg_for_blend_list))):
        ## open img
        img_src_pil = Image.open(img_file)
        img_src = np.array(img_src_pil)
        img_src = cv2.cvtColor(img_src, cv2.COLOR_RGBA2RGB)
        bg_src_pil = Image.open(bg_file)
        bg_src = np.array(bg_src_pil)
        bg_src = cv2.cvtColor(bg_src, cv2.COLOR_RGBA2RGB)
        #print(bg_src.shape)
        #print(img_src.shape)
        src_w, src_h = img_src.shape[1], img_src.shape[0]
        xfile = pathlib.PosixPath(src1, '.'.join((img_file.split('/')[-1].split('.')[0], 'xml')))
        #print(xfile)
        #print(img_file)
        xml_keys = ET.parse(xfile)
        root = xml_keys.getroot()

        for obj in root.findall('object'):
            bndbox_anno = obj.find('robndbox')
            #print(bndbox_anno)
            wh_list = [bndbox_anno.find(tag).text for tag in ['w', 'h']]
            wh_list = np.array(wh_list, dtype=np.float).astype(np.int)
            ## get padding dims wrt to bbox h w
            #pad_w, pad_h = get_pad_size(wh_list, bin_pat[idx])

            img_content = crop(content_wh, img_src)

        ## reshape the bg to fit the src image
        bg_resized = cv2.resize(bg_src, (src_w, src_h), cv2.INTER_CUBIC)
        #print(bg_resized.shape)
        assert bg_resized.shape == img_src.shape
        ## blend
        img_blended = 0.5 * img_src + 0.5 * bg_resized
        ## unpack the content on the blended image
        w, h = wh_list
        cx, cy = cxcy_list
        start_x = cx - w // 2
        start_y = cy - h // 2
        img_blended[start_y:start_y+h, start_x:start_x+w] = img_content
        #print(img_blended.shape)
        #print(dst.shape)
        ## copy the images and xml to destination
        dst_xfile = pathlib.PurePath(dst, xfile.as_posix().split('/')[-1]).as_posix()
        shutil.copyfile(xfile, dst_xfile)
        img_blended_pil = Image.fromarray(np.uint8(img_blended))
        img_blended_pil.save(pathlib.PurePath(dst, img_file.split('/')[-1]).as_posix())
    
blend_imgs('../train_single_0_90_180_270_bordered_corrected', '../CardBackground', '../debug_data')