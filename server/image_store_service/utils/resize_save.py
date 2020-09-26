import pure_utils as pu
import numpy as np
import cv2
from PIL import Image
from tqdm import tqdm

def resize_save(img_dir, ratio):
    img_path_list = pu.get_img_paths(img_dir)
    for img_path in tqdm(img_path_list):
        img_pil = Image.open(img_path)
        img = np.array(img_pil)
        new_height = img.shape[0] // ratio
        new_width = img.shape[1] // ratio
        new_size = (new_width, new_height)
        new_img = cv2.resize(img, new_size, cv2.INTER_CUBIC)
        #print(img.shape)
        #print(new_img.shape)
        new_img_pil = Image.fromarray(new_img)
        new_img_pil.save(img_path)


#resize_save('../Organized_Data_Cards/Training/debug_data/', 3)
