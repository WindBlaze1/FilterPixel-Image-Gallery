from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from googleapiclient.discovery import build
from django.conf import settings

def display_images(request):
    # Initialize the Google Drive API service
    
    drive_service = build('drive', 'v3', developerKey=settings.GOOGLE_DRIVE_API_KEY)

    folder_id = '1_qOJ0z3kI_e2IJq4X6HqF0T1ROBESygS' # The public Images URL

    images_per_page = 12

    page = int(request.GET.get('page', 1))

    # Calculate the starting index based on the page number and images per page
    start_index = (page - 1) * images_per_page

    response = drive_service.files().list(
        q=f"'{folder_id}' in parents",
        fields='files(id, name)',
        pageSize=images_per_page,
        pageToken=None if page == 1 else request.GET.get('nextPageToken', None)
    ).execute()

    image_urls = []
    for file in response.get('files', []):
        image_urls.append(f"https://drive.google.com/uc?id={file['id']}")

    next_page_token = response.get('nextPageToken')

    return render(request, 'image_template.html', {
        'image_urls': image_urls,
        'page': page,
        'next_page_token': next_page_token,
    })


@login_required
def show_gallery(request):
    return render(request, 'gallery.html')