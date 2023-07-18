from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from googleapiclient.discovery import build
from django.core.paginator import Paginator
from django.conf import settings

def fetch_drive_images(request):
    drive_service = build('drive', 'v3', developerKey=settings.GOOGLE_DRIVE_API_KEY)

    folder_id = '1_qOJ0z3kI_e2IJq4X6HqF0T1ROBESygS' # The public Images URL

    images_per_request = 12

    # If None: means this is first page
    next_page_token = request.GET.get('next_page_token')

    response = drive_service.files().list(
        q=f"'{folder_id}' in parents",
        fields='files(id, name)',
        pageSize=images_per_request,
        pageToken=next_page_token,
    ).execute()

    image_urls = []
    for file in response.get('files', []):
        image_urls.append(f"https://drive.google.com/uc?id={file['id']}")

    next_page_token = response.get('nextPageToken')

    return JsonResponse({
        'image_urls': image_urls,
        'next_page_token': next_page_token,
    })


@login_required
def show_gallery(request):
        if request.method == 'POST':
            button = request.POST.get('button')
            if button == 'drive':
                images = ['image1.jpg', 'image2.jpg', 'image3.jpg', ...]  # List of all images for Button 1
            elif button == 's3':
                images = ['image4.jpg', 'image5.jpg', 'image6.jpg', ...]  # List of all images for Button 2
            else:
                images = []
        else:
            images = []

        paginator = Paginator(images, 12)  # Number of images to display per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'gallery.html', {'page_obj': page_obj})