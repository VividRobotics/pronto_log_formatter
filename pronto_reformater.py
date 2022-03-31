import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='',
    aws_access_key_id='xxxx',
    aws_secret_access_key='xxx'
)

for bucket in s3.buckets.all():
    print(bucket.name)