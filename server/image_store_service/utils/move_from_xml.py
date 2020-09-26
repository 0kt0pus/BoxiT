##This is an improved version of the move selected
import xml.etree.ElementTree as ET
import pure_utils as pu
import os
from tqdm import tqdm

def move_from_xml(img_dir, req_classes, dst_dir, include_xml=False):
    ## get the xmls
    xml_file_list = pu.get_xml_paths(img_dir)
    ## get the image files
    img_file_list = pu.get_img_paths(img_dir)
    ## the img file name ls
    img_file_name_list = [os.path.splitext(f.split('/')[-1])[0] for f in img_file_list]
    #print(img_file_name_list)
    ## dict to hold file-class assositation
    xfile_class_dict = dict()
    ## iterate, open and get the object class
    for xfile in tqdm(xml_file_list):
        xml_keys = ET.parse(xfile)
        root = xml_keys.getroot()
        ## get the objects
        class_list = list()
        for obj in root.findall('object'):
            name = obj.find('name')
            class_list.append(name.text)
        ## update the file-class dict
        xfile_class_dict[xfile] = class_list
    ## now we have the file-class association, so iterate over it
    ## and filter out the files that does not have req_classes
    req_file_list = list()
    for k, v in xfile_class_dict.items():
        #print(k, v)
        if list(map(lambda x: x in req_classes, v))[0] == True:
            req_file_list.append(k)
    ## get the file names of required
    req_file_name_list = [os.path.splitext(f.split('/')[-1])[0] for f in req_file_list]
    ## map the req files
    req_img_bool_list = list(map(lambda x: x in req_file_name_list, img_file_name_list))
    ## filter the false and keep the True so we have the req img file (only true idxs)
    req_img_list = [img_file_list[i] for i, j in enumerate(req_img_bool_list) if j == True]
    #print(len(req_img_list))
    #print(len(req_file_list))
    assert len(req_img_list) == len(req_file_list)
    #print(req_file_list)
    #for f in req_file_list:
    #      print(f)
    if not include_xml:
        pu.mover(req_img_list, dst_dir)
        #return req_img_list
    else:
        pu.mover(req_img_list, dst_dir)
        pu.mover(req_file_list, dst_dir)
        #return (req_img_list, req_file_list)


req_card_types = ['AT', 'BC', 'PA', 'FSPI']
req_sides = ['A', 'B']
req_angles = ['0', '90', '180', '270']
#req_angles = ['0', '20', '40', '60', '80', '90', '180', '270']

req_class_list = ['_'.join([c_ty, c_sd, c_ag]) 
                            for c_ty in req_card_types
                                for c_sd in req_sides
                                    for c_ag in req_angles]

## annotate image names
#pu.annotate_name('/media/FourT/uniquare/local/normalizedSingleSeptember/Training/modeA', 
#                    '_modeC_up_right')
move_from_xml('/media/FourT/uniquare/local/normalizedSingleSeptember/Testing/modeA', 
                req_class_list,
                '/media/FourT/uniquare/local/uniquare_multilables/tfod2/workspace/inference/inputs_mode_A_norm_ortho/',
                include_xml=True,
                )

