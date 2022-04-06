import boto3
import json
import os

os.mkdir("./temp_files")

with open("./AWS_Credentials.json", "r") as data:
    credentials = json.load(data)

#Creating AWS session
session = boto3.Session(
    aws_access_key_id=credentials["access_key_id"],
    aws_secret_access_key=credentials["secret_access_key"])

#Establishing session resource
s3 = session.resource("s3")

bucket = s3.Bucket("pronto-logs-ftp")

bucket_folder = "dez-pronto-log-dev"

