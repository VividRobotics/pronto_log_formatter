import boto3
import json
import os

def s3_uploader(bucket, bucket_folder):
    """
    input: 
        * s3.Bucket() object
        * bucket_folder - a folder inside s3.Bucket() object
    """    
    #Establishing list of object names within bucket object
    object_keys = [object.key for object in bucket.objects.filter(Prefix=bucket_folder)]

    #Establishing list of object names
    object_file_names = [object.split("/")[1] for object in object_keys][1:]

    #removing blank value
    object_keys = object_keys[1:]

    print(object_keys, object_file_names)
    #Uploading folder contents from bucket to temperary folder
    #[bucket.upload_file(object_keys[x], f"./temp_files/processed/{object_file_names[x]}") for x in range(len(object_keys))]