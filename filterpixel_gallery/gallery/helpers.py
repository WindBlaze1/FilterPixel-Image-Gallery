from googleapiclient.discovery import build
import boto3
from botocore import UNSIGNED
from botocore.config import Config

def get_drive_urls(folder_id='1_qOJ0z3kI_e2IJq4X6HqF0T1ROBESygS'):
    api_key = "AIzaSyC9ZSbJEK7JvtwU1b5nUK6HpKFY9yRSdxw"

    drive_service = build('drive', 'v3', developerKey=api_key)

    file_urls = []

    page_token = None
    while True:
        response = drive_service.files().list(q="'{}' in parents".format(folder_id),
                                            fields="nextPageToken, files(id, name)",
                                            pageSize=1000,
                                            pageToken=page_token).execute()
        files = response.get('files', [])
        
        # Print the URLs of all files in the batch
        for file in files:
            file_url = "https://drive.google.com/uc?export=view&id={}".format(file['id'])
            file_urls.append(file_url)

        # Check if there are more files, and retrieve the next page if necessary
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return file_urls

def get_s3_urls():
    
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    my_bucket = s3.Bucket('testbucketfp')

    folder_path = '' # Present in bucket without any folder

    files_url = []

    for obj in my_bucket.objects.filter(Prefix=folder_path):
        if obj.key != folder_path:
            url = f"https://{my_bucket.name}.s3.amazonaws.com/{obj.key}"
            files_url.append(url)

    return files_url

# print(get_drive_urls())