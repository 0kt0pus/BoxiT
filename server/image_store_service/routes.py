from flask import Blueprint, request, jsonify
import json
import os
import sys
from bson import ObjectId
import utils.pure_utils as pu

## JsonEncoder manage mongodb objectId
class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        ## if there is an instant of an object ID return
        ## a str of it
        if isinstance(o, ObjectId):
            return str(o)

        return json.JSONEncoder.default(self, o)

## blueprints for the create item
createRoute = Blueprint("create", __name__)

## Route to create a project
@createRoute.route("/api/create", methods=["POST"])
def create():
    print(request, flush=True) 
    ## decompose the recieved request
    name = request.json.get("name")
    description = request.json.get("description")
    path = request.json.get("path")

    ## create a python dict from the request to store in MongoDB
    item = {
        "name": name,
        "description": description,
        "path": path,
    }
    ## insert the dict to db collection
    #collection.insert_one(item)
    ## get the folder path and load all files
    project_path = item["path"]
    img_paths = pu.get_img_paths(project_path)
    xml_paths = pu.get_xml_paths(project_path)
    '''
    for p in img_paths:
        print(p)
    print()
    for p in xml_paths:
        print(p)
    '''
    #print(project_path)
    img_names = [pu.get_file_name(path) for path in img_paths]
    xml_names = [pu.get_file_name(path) for path in xml_paths]
    #print(xml_names)
    ## generate a list of dicts containing img name and corresponding xml name 
    path_obj_list = list()
    for xml_p, xml_n in zip(xml_paths, xml_names):
        path_obj = dict()
        #print(img_names.index(xml_n))
        #print(img_paths[img_names.index(xml_n)])
        path_obj["image_path"] = img_paths[img_names.index(xml_n)]
        path_obj["annotation_path"] = xml_p
        path_obj_list.append(path_obj)

    #print(path_obj_list)
    project_data = {
        "project_name": item["name"],
        "project_description": item["description"],
        "data_paths": path_obj_list,
    }
    with open("./data/project_data.json", 'w') as f:
        json.dump(project_data, f)


    return jsonify(data="Item create sucessfully")