import boto3
import json
import os

with open("./config.json", "r") as data:
    config = json.load(data)
    
def s3_deleter(resource, bucket, bucket_folder):
    """
    input: 
        * s3.Bucket() object
        * bucket_folder - a folder inside s3.Bucket() object
    """

    #Establishing list of object names within bucket object
    object_keys = [object.key for object in bucket.objects.filter(Prefix=bucket_folder)]

    #removing blank value
    object_keys = object_keys[1:]

    #Deleting old files from bucket folder
    [resource.Object(config["bucket_name"], object_keys[x]).delete() for x in range(len(object_keys))]