from flask import Blueprint, request, jsonify
import json
import os
import sys
from bson import ObjectId

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
    print(item)

    return jsonify(data="Item create sucessfully")