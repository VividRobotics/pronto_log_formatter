import boto3
import json
import os

#os.mkdir("./temp_files")

with open("./AWS_Credentials.json", "r") as data:
    credentials = json.load(data)

#Creating AWS session
session = boto3.Session(
    aws_access_key_id=credentials["access_key_id"],
    aws_secret_access_key=credentials["secret_access_key"]
)

#Establishing session resource
s3 = session.resource("s3")

target_bucket = s3.Bucket("pronto-logs-ftp")

#Establishing list of object names within bucket object
object_keys = [object.key for object in target_bucket.objects.filter(Prefix="dez-pronto-log-dev")]

object_file_names = [object[19:] for object in object_keys][1:]

#removing blank value
object_keys = object_keys[1:]

#Downloading folder contents from bucket to temperary folder
[target_bucket.download_file(object_keys[x], f"./temp_files/{object_file_names[x]}") for x in range(len(object_keys))]

#Deleting temperary files
#os.rmdir("temp_files")