import random
import shutil

import cv2
from tqdm import tqdm
import albumentations as A
from matplotlib import pyplot as plt
import pure_utils as pu
from PIL import Image
import numpy as np
from data_loader import PascalVocDataLoader

BOX_COLOR = (255, 0, 0) # Red
TEXT_COLOR = (255, 255, 255) # White
DATA_DIR = '../../Organized_feed_data/Training/Mode_A_B_PA_B_only_aug/'
SAVE_DIR = '../../Organized_feed_data/Training/Mode_A_B_PA_B_only_auged'
def visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, x_max, y_max = bbox
    x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)
    #x_min, x_max, y_min, y_max = int(x_min), int(x_min + w), int(y_min), int(y_min + h)
    print(img.shape)
    #print(bbox)
    #print(bbox)
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)

    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    #cv2.rectangle(img, (x_min, y_min - 100), (x_min, y_min), BOX_COLOR, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(0.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35, 
        color=TEXT_COLOR, 
        lineType=cv2.LINE_AA,
    )
    return img


def visualize(image, bboxes, category_ids, category_id_to_name):
    img = image.copy()
    for bbox, category_id in zip(bboxes, category_ids):
        class_name = category_id_to_name[category_id]
        img = visualize_bbox(img, bbox, class_name)
    plt.figure(figsize=(12, 12))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

#image = cv2.imread('/Users/melukadesilva/Documents/Research_assistant_work/uniquare/phase_4_progress/data/train_single/AT_A_0_im_0.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#print(image.shape)
#cxcywha_list = [528, 352, 976, 625, 0.0]
#cxcywha_list = [869, 591, 1531.0, 970.0, 6.283185307179586]
#cxcywh_list = pu.rot2square(cxcywha_list)
#bboxes = [pu.tlbr(cxcywh_list)]
category_ids = [1]
#category_id_to_name = {17: 'BC_A_0'}
#print(bboxes)
#visualize(image, bboxes, category_ids, category_id_to_name)
def construct_pipe(transforms_list: list) -> A.Compose:
    transform = A.Compose(
        transforms_list,
        bbox_params=A.BboxParams(format="pascal_voc", label_fields=['category_ids'])
    )
    return transform

#random.seed(6)
#transformed = transform(image=image, bboxes=bboxes, category_ids=category_ids)
## load img, box pairs, and run through the augmentation pipeline and save them to a
## new folder
## consume the loader and get the max box w,h
data_loader = PascalVocDataLoader(data_dir=DATA_DIR)

'''
w_list = list()
h_list = list()
for _, _, _, cxcywh in tqdm(data_loader):
    _, _, w, h = cxcywh
    w_list.append(w)
    h_list.append(h)

w_sorted_list = sorted(w_list)
h_sorted_list = sorted(h_list)
print(w_list[0])
print(w_sorted_list[0])
transform_pipe = construct_pipe(tr_list)
'''
transform = construct_pipe([ 
    ##A.IAASuperpixels(p=0.3),
    ##A.RandomCropNearBBox(p=1),
    A.RandomBrightnessContrast(p=1),
    #A.RandomSizedBBoxSafeCrop(height=600, width=800),
    A.MotionBlur(blur_limit=40, p=1),
    #A.GaussianBlur(p=1, blur_limit=21),
    A.GaussNoise(p=1, always_apply=True, mean=0, var_limit=(10.0, 50.0))
    ])

for image, bboxes, img_path, _ in tqdm(data_loader):
    transformed = transform(image=image, bboxes=bboxes, category_ids=category_ids)
    #print(transformed['image'].shape)
    save_img_path = pu.change_dst_dir(img_path, SAVE_DIR)
    #print(save_path)
    save_xml_path = pu.change_ext(save_img_path, 'xml')
    src_xml_path = pu.change_ext(img_path, 'xml')
    ## coy the xml files
    shutil.copyfile(src_xml_path, save_xml_path)
    #cv2.imwrite(save_img_path, transformed['image'])
    img_pil = Image.fromarray(np.uint8(transformed['image']))
    img_pil.save(save_img_path)

'''
img = Image.fromarray(np.uint8(transformed['image']))
img.save('/Users/melukadesilva/Documents/Research_assistant_work/uniquare/phase_4_progress/data/debug_data/AT_A_0_im_0.jpg')

visualize(
    transformed['image'],
    transformed['bboxes'],
    transformed['category_ids'],
    category_id_to_name
)
'''