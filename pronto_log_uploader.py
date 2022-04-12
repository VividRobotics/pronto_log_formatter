import os

def s3_uploader(s3, bucket, bucket_folder):
    """
    input: 
        * s3.Bucket() object
        * bucket_folder - a folder inside s3.Bucket() object
    """    
    final_files = os.listdir("./temp_files/formatted")

    for file in final_files:
        route = f"./temp_files/formatted/{file}"
        bucket.upload_file(route, file)