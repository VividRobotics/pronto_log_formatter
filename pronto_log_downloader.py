def s3_downloader(bucket, bucket_folder):
    """
    input: 
        * s3.Bucket() object
        * bucket_folder 

    output: 
        * folder object
        """
        
    #Establishing list of object names within bucket object
    object_keys = [object.key for object in bucket.objects.filter(Prefix=bucket_folder)]

    object_file_names = [object.split("/")[1] for object in object_keys][1:]

    #removing blank value
    object_keys = object_keys[1:]

    #Downloading folder contents from bucket to temperary folder
    [bucket.download_file(object_keys[x], f"./temp_files/raw/{object_file_names[x]}") for x in range(len(object_keys))]