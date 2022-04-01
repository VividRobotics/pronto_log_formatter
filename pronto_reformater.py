import boto3
import json

with open("./credentials.json", "r") as data:
    credentials = json.load(data)

s3 = boto3.resource(
    service_name="s3", 
    region_name=credentials["region_name"], 
    aws_access_key_id=credentials["access_key_id"],
    aws_secret_access_key=credentials["secret_access_key"]
)

for bucket in s3.buckets.all():
    print(bucket.name)