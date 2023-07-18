import googleapiclient.discovery
from django.conf import settings
from requests import HTTPError

def get_images_from_google_drive(folder_url='https://drive.google.com/drive/folders/1_qOJ0z3kI_e2IJq4X6HqF0T1ROBESygS?usp=sharing'):
    
    GOOGLE_DRIVE_API_KEY = 'AIzaSyC9ZSbJEK7JvtwU1b5nUK6HpKFY9yRSdxw'
    
    try:
        # Extract the folder ID from the URL
        folder_id = folder_url.split('/')[-1]

        # Create a Google Drive API client
        drive_service = googleapiclient.discovery.build('drive', 'v3', GOOGLE_DRIVE_API_KEY)

        # Retrieve the list of files in the folder
        files = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()

        # Extract the image URLs from the files list
        image_urls = []
        for file in files['files']:
            if file['name'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Generate the image URL using the file ID
                image_url = f"https://drive.google.com/uc?id={file['id']}"
                image_urls.append(image_url)

        return image_urls

    except HTTPError as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == '__main__':
    print(get_images_from_google_drive())