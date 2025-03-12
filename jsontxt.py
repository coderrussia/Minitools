#import
import os
import json

#script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

#json folder
json_folder_name = "json"
json_folder_path = os.path.join (script_dir, json_folder_name)
#crete
if not os.path.exists(json_folder_path):
    os.mkdir(json_folder_path)

#txt folder
txt_folder_name = "txt"
txt_folder_path = os.path.join (script_dir, txt_folder_name)
#create
if not os.path.exists(txt_folder_path):
    os.mkdir(txt_folder_path)

#json file
json_file_name = "file.json"
json_file_path = os.path.join(json_folder_path, json_file_name)

#txt file
txt_file_name = "file.txt"
txt_file_path = os.path.join(txt_folder_path, txt_file_name)


# Read json
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_content = json_file.read()

#write txt

with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(json_content)