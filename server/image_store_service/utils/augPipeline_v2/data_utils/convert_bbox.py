import xml.etree.ElementTree as ET
import numpy as np
from pure_utils import *
from PIL import Image, ImageDraw

def convert_rot2square(img_dir: str):
    img_file_list = get_img_paths(img_dir)
    
    for idx, img_file in enumerate(img_file_list):
        xfile = pathlib.PosixPath(img_dir, '.'.join((img_file.split('/')[-1].split('.')[0], 'xml')))
        #print(xfile)
        #print(img_file)
        xml_keys = ET.parse(xfile)
        root = xml_keys.getroot()
        img = Image.open(img_file)
        for obj in root.findall('object'):
            bndbox_anno = obj.find('robndbox')
            #print(bndbox_anno)
            cxcywha_list = [float(bndbox_anno.find(tag).text)-1 for tag in ['cx', 'cy', 'w', 'h']]
            angle = float(bndbox_anno.find('angle').text)
            cxcywha_list.append(angle)
            #print(np.degrees(angle))
            print(cxcywha_list)
            cxcywh_list = rot2square(cxcywha_list)
            print(cxcywh_list)
            ## top-left bottom-right 
            tlbr_list = list(tlbr(cxcywh_list))
            #print(tlbr_list)
            # draw the box
            #draw = ImageDraw.Draw(img)
            #draw.rectangle(tlbr_list, outline="red")
            #img.save(pathlib.PurePath(img_dir, 'test.png').as_posix())
            

convert_rot2square('../debug_data')