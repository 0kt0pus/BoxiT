import os
import pathlib

def flatten(list_2d: list) -> list:
    flatten = lambda l: [item for sub_list in l for item in sub_list]
    flat_list = flatten(list_2d)
    return flat_list
    
def get_unique_values(values: list) -> list:
    unique_values = list()
    for val in values:
        if val not in unique_values:
            unique_values.append(val)

    return unique_values

def get_valid_exts(data_dir:str, ext_list: list) -> list:
    ## filter function that returns only valid exts
    def ext_filter(ext):
        if (ext in ext_list):
            return True
        else:
            return False
    ## all the paths
    file_list = []
    for root, subdir, files in os.walk(data_dir):
        for f in files:
            file_list.append(pathlib.PurePath(root, f).as_posix())
    ## get all the available extensions
    all_ext_list = list(map(lambda x: os.path.splitext(x)[-1].split('.')[-1], file_list))
    #print(all_ext_list)
    ## filter only the valid ones
    valid_ext_list = list(filter(ext_filter, all_ext_list))
    unique_ext_list = get_unique_values(valid_ext_list)
    #print(valid_ext_list)
    return unique_ext_list

def get_ext_paths(data_dir: str, ext: str) -> list:
    #   print(data_dir)
    ## filter function that returns only valid exts
    def ext_filter(path):
        now_ext = os.path.splitext(path)[-1].split('.')[-1]
        #print(now_ext)
        if (now_ext == ext):
            return True
        else:
            return False
    file_list = []
    for root, subdir, files in os.walk(data_dir):
        for f in files:
            file_list.append(pathlib.PurePath(root, f).as_posix())

    ## filter all the exts except for the required one
    required_path_list = list(filter(ext_filter, file_list))
    #print(required_path_list)
    return required_path_list

'''
## dummy test
EXT_LIST = ['jpg', 'png', 'jpeg']
data_dir = '/Users/melukadesilva/Documents/Research_assistant_work/uniquare/phase_4_progress/data/val'
valid_exts = get_valid_exts(data_dir, EXT_LIST)
path_list = [get_ext_paths(data_dir, ext) for ext in valid_exts]
flat_list = flatten(path_list)
print(flat_list)
#print(path_list[1])
'''