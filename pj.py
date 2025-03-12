import pandas as pd
import os


#script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

#json folder
json_folder_name = "json"
json_folder_path = os.path.join (script_dir, json_folder_name)

#json folder create
if not os.path.exists(json_folder_path):
    os.mkdir(json_folder_path)

#parquet folder create
parquet_folder_name = "parquet"
parquet_folder_path = os.path.join (script_dir, parquet_folder_name)
if not os.path.exists(parquet_folder_path):
    os.mkdir(parquet_folder_path)

#parquet file
parquet_file_name = "file.parquet"
parquet_file_path = os.path.join(script_dir, parquet_folder_path, parquet_file_name)

#json file
json_file_name = "file.json"
json_file_path = os.path.join(json_folder_path, json_file_name)


parquet_processing = pd.read_parquet(parquet_file_path)

parquet_processing.to_json(json_file_path, orient='records', lines=True)