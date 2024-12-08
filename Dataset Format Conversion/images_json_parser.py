import json
import os

'''

IMAGE DATA

id - from the file name (initial 6 digits.)
height - from the image json
width - from the image json
file_name - as it is.

-------------------------------------------------

ANNOTATIONS DATA

!! Do only if `draw : TRUE`

id - global_counter for all annotations in utils.json
category_id - (from categories.json)
image_id - associated image id
segmentation - list of all annotation points : [[x-cord,y-cord,x-cord,y-cord...]]
bbox - [x,y,width,height]
area - area of the segmentation
iscrowd - 0

'''

# Update PATH to change location for checking json file.
path_to_dir = "Dataset Format Conversion/test ground/"

files = os.listdir(path_to_dir)
for file in files : 

    # Reading individual files.

    with open(path_to_dir + file, "r") as file_obj : 
        file_data = json.load(file_obj)

    file_image_data = {
        "id" : None,
        "height" : None,
        "width" : None,
        "file_name" : None
    }

    file_annotation_data = []

    # Extracting Image Data

    file_image_data["id"] = file[:6]
    file_image_data["file_name"] = file
    file_image_data["height"] = file_data["imgHeight"]
    file_image_data["width"] = file_data["imgWidth"]


    # Extracting Annotations Data

    for object in file_data["objects"] : 

        file_annotation_data_template = {
            "id" : None,
            "category_id" : None,
            "image_id" : None,
            "segmentation" : None,
            "bbox" : None,
            "area" : None,
            "iscrowd" : None,
        }

        if not object["draw"] : continue

        file_annotation_data_template["id"] = None
        file_annotation_data_template["category_id"] = None
        file_annotation_data_template["image_id"] = file_image_data["id"]
        file_annotation_data_template["segmentation"] = None
        file_annotation_data_template["bbox"] = None
        file_annotation_data_template["area"] = None
        file_annotation_data_template["iscrowd"] = 0


    print(file_image_data)