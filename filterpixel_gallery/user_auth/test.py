import boto3
import botocore
import os
from botocore import UNSIGNED
from botocore.config import Config

os.environ['AWS_DEFAULT_REGION'] = "ap-south-1"

s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
my_bucket = s3.Bucket('testbucketfp')

folder_path = '' # Present in bucket without any folder

files_url = []

for obj in my_bucket.objects.filter(Prefix=folder_path):
    if obj.key != folder_path:
        url = f"https://{my_bucket.name}.s3.amazonaws.com/{obj.key}"
        files_url.append(url)

return files_url