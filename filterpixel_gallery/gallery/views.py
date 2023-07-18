from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from gallery.helpers import get_drive_urls, get_s3_urls

@login_required
def show_gallery(request):
        print(request.method)
        if request.method == 'POST':
            button = request.POST.get('button')
            print('selected:',button)
            if button == 'drive':
                images = get_drive_urls()
                s3_active = ''
                drive_active = 'active'
            elif button == 's3':
                images = get_s3_urls()
                s3_active = 'active'
                drive_active = ''
        else:
            images = get_s3_urls()
            s3_active = 'active'
            drive_active = ''


        paginator = Paginator(images, 6)  # Number of images to display per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'gallery.html', {'page_obj': page_obj, 's3_active':s3_active,'drive_active':drive_active})