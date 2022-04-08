from concurrent.futures import process
import boto3
import json
import os
import pronto_log_downloader
import pronto_log_deleter
import pronto_log_reformater
import pronto_log_uploader

os.mkdir("./temp_files")
os.mkdir("./temp_files/raw")
os.mkdir("./temp_files/formatted")

with open("./AWS_Credentials.json", "r") as data:
    credentials = json.load(data)

with open("./config.json", "r") as data:
    config = json.load(data)

#Creating AWS session
session = boto3.Session(
    aws_access_key_id=credentials["access_key_id"],
    aws_secret_access_key=credentials["secret_access_key"])

#Establishing session resource
s3 = session.resource("s3")

raw_bucket = s3.Bucket(config["raw_bucket"])
processed_bucket = s3.Bucket(config["processed_bucket"])

raw_bucket_folder = config["raw_bucket_folder"]
processed_bucket_folder = config["processed_bucket_folder"]

pronto_log_downloader.s3_downloader(raw_bucket, raw_bucket_folder)
#pronto_log_deleter.s3_deleter(s3, raw_bucket, raw_bucket_folder)

#Creating a list of all available .txt files
files = os.listdir("./temp_files/raw")

#Iterating over all files in raw folder
[pronto_log_reformater.file_reformater(file) for file in files]

#Uploading formatted files to s3
#TODO TODO TODO TODO
#https://www.developerfiles.com/upload-files-to-s3-with-python-keeping-the-original-folder-structure/
[pronto_log_uploader.s3_uploader(processed_bucket, processed_bucket_folder)]

#Removing original files from temp folder
#[os.remove(f"./temp_files/raw/{file}") for file in files]