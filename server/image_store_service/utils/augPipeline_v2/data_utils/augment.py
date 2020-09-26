import cv2
from skimage.exposure import rescale_intensity
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io
import numpy as np
from tqdm import tqdm

import os
import pathlib
from PIL import Image
import shutil


input_folder = '/media/FourT/uniquare/local/TensorFlow/workspace/training_demo/images/Cards_Balanced_Dataset_v2_bak'
output_folder = '/media/FourT/uniquare/local/TensorFlow/workspace/training_demo/images/Cards_Balanced_Dataset_v2_Aug_13'
extension=".png"

img_dir = '../train_single_0_90_180_270_bordered_corrected'
dst_dir = '../train_single_0_90_180_270_bordered_augmented_3_rgb_temp'
num_times = 3

#blur_param_list = [(i, j) for i in [3, 5, 7, 11, 13, 15] for j in [0.7, 0.9, 1.2, 1.8]]
blur_param_list = [(i, j) for i in [13, 15] for j in [0.7, 1.2]]
print(blur_param_list)
print()
'''
def main():
    i =0

    for filename in sorted(os.listdir(input_folder)): 
        
        if filename.endswith(extension):
            #print(input_folder+filename)
            img = cv2.imread(os.path.join(input_folder,filename))
            #print(img.shape)
            image = cv2.GaussianBlur(img,(13,13),0.2)
      
            cv2.imwrite(os.path.join(output_folder,filename), image) 
'''
def main():
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
            file_path = pathlib.PurePath(img_dir, name)
            file_list.append(file_path.as_posix())
    img_file_list = list(filter(filter_xmls, file_list))

    ## make folders for each aug combo
    #dir_path_list = list()
    '''
    for (k, sig) in blur_param_list:
        ## make path
        folder_name = 'aug_' + str(k) + '_' + ''.join(str(sig).split('.'))
        dir_path = pathlib.PurePath(dst_dir, folder_name)
        ## if dir does not exists make it
        if not os.path.isdir(dir_path):
            ## make the dir
            os.mkdir(dir_path)
        dir_path_list.append(dir_path)
    '''
    ## do the augmentations and save the files along with the corresponding xml
    for img_file in tqdm(img_file_list):
        ## open image
        img = cv2.imread(img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        xml_file = '.'.join([os.path.splitext(img_file)[0], 'xml'])
        #print(xml_file)
        ## for a list of blur kernel sigma levels
        for (k, sig) in blur_param_list:
            folder_name = 'aug_' + str(k) + '_' + ''.join(str(sig).split('.'))
            dir_path = pathlib.PurePath(dst_dir, folder_name)
            ## if dir does not exists make it
            if not os.path.isdir(dir_path):
                ## make the dir
                os.mkdir(dir_path)
            #dir_path_list.append(dir_path)
            ## add the aug
            img = cv2.GaussianBlur(img, (k, k), sig)
            if num_times != 0:
                #print(num_times)
                for i in range(num_times-1):
                    img = cv2.GaussianBlur(img, (k, k), sig)
            ## save the new image in the new folder with a new name
            #print(pathlib.Path(img_file).suffix)
            img_new_file =  os.path.split(os.path.splitext(img_file)[0] + '_aug_' + str(k) + '_' + ''.join(str(sig).split('.')) + pathlib.Path(img_file).suffix)[-1]
            ## save image
            img_pil = Image.fromarray(img)
            img_pil.save(pathlib.PurePath(dir_path, img_new_file).as_posix())
            #print(img_new_file)
            ## save the corresponding  xml file
            xml_new_file = os.path.split(os.path.splitext(img_file)[0] + '_aug_' + str(k) + '_' + ''.join(str(sig).split('.')) + '.xml')[-1]
            shutil.copyfile(xml_file, pathlib.PurePath(dir_path, xml_new_file).as_posix())
            
    
# Driver Code 
if __name__ == '__main__': 
    main() 

