from pure_utils import *
import shutil
import os
import pathlib
from tqdm import tqdm

def move_selected(img_dir: str, 
                    dst_dir: str,
                    req_card_types: list, 
                    req_sides: list, 
                    req_angles: list,
                    write_lables: bool=False, 
                    include_xml: bool=False):
                    
    if include_xml:
        ## get the list of available images
        img_path_list = get_all_paths(img_dir)
    else:
        img_path_list = get_img_paths(img_dir)
    ## construct the required class name list
    req_class_list = ['_'.join([c_ty, c_sd, c_ag]) 
                            for c_ty in req_card_types
                                for c_sd in req_sides
                                    for c_ag in req_angles]
    #print(req_class_list)
    ## filter out the items not in the req lists
    req_out_bool_list = filter_list(img_path_list, req_class_list)
    idx_list = [idx for idx, val in enumerate(req_out_bool_list) if val == True]
    #print(idx_list)
    ## collect all the corresponding images
    req_img_path_list = [img_path_list[idx] for idx in idx_list]
    #print(req_img_path_list)
    ## copy the img files along with their xmls to new destination
    for src_img in tqdm(req_img_path_list):
        dst_img = pathlib.PurePath(dst_dir, src_img.split('/')[-1]).as_posix()
        #print(src_img)
        #print(dst_img)
        #print()
        #shutil.copyfile(src_img, dst_img)
        #print(os.path.splitext(src_img)[:-1])
        shutil.copyfile(src_img, dst_img)
        if include_xml:
            src_xml = '.'.join([os.path.splitext(src_img)[:-1][0], 'xml'])
            dst_xml = pathlib.PurePath(dst_dir, src_xml.split('/')[-1])
            #print(src_xml)
            #print(dst_xml)
            #print()        
            shutil.copyfile(src_xml, dst_xml)
    ## write the lable map for the new data
    if write_lables:
        ## lable map will be in data_utils/annotations
        write_label_map_v1(req_class_list)
    
#annotate_name('../debug_data', 'alpha_aug')
#req_card_type = ['AT', 'BC', 'PA', 'FSPI']
#req_sides = ['A', 'B']
#req_angles = ['0', '90', '180', '270']

req_card_type = ['AT', 'BC', 'PA', 'FSPI']
req_sides = ['A', 'B']
#req_angles = ['0', '90', '180', '270']
req_angles = ['0', '20', '40', '60', '80', '90', '180', '270']
#req_angles = ['0', '20', '40', '60', '80', '90', '100', '120', '140', '160', '180', '200', '220', '240', '260', '270', '280', '300', '320', '340']
#req_angles = ['0', '20', '40', '60', '80', '90']
'''
req_class_list = ['_'.join([c_ty, c_sd, c_ag]) 
                            for c_ty in req_card_type
                                for c_sd in req_sides
                                    for c_ag in req_angles]
print(len(req_class_list))
'''
'''
req_card_type = ['AT', 'BC', 'PA', 'FSPI']
req_sides = ['A', 'B']
#req_angles = ['0', '90', '180', '270']
req_angles = ['0', '20', '40', '60', '80', '90', '100', '120', '140', '160', '180', '200', '220', '240', '260', '270', '280', '300', '320', '340']
'''
'''
move_selected('../Organized_Data_Cards/Training/ModeC/modeC_20/C2_5', '../Organized_feed_data/Training/Mode_A_B_C_all_pos_quadrat/modeC_2_5', req_card_types=req_card_type, 
                    req_sides=req_sides, req_angles=req_angles, write_lables=False, include_xml=True)
annotate_name('../Organized_feed_data/Training/Mode_A_B_C_all_pos_quadrat/modeC_2_5', "C_2_5_quadrat")
'''
move_selected('/media/FourT/uniquare/local/data/Organized_Data_Cards/Testing/Testing_C1_2', '/media/FourT/uniquare/local/uniquare_multilables/tfod2/workspace/inference/inputs_mode_C_1_2_quadrat', req_card_types=req_card_type, 
                    req_sides=req_sides, req_angles=req_angles, write_lables=False, include_xml=False)