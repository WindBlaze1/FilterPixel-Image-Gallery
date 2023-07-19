from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from gallery.helpers import get_drive_urls, get_s3_urls

@login_required
def show_gallery_drive(request):
    images = get_drive_urls()
    # print(images)
    paginator = Paginator(images, 6)  # Number of images to display per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {'page_obj': page_obj,'s3':'','drive':'active'})

@login_required
def show_gallery_s3(request):
    images = get_s3_urls()
    paginator = Paginator(images, 6)  # Number of images to display per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery.html', {'page_obj': page_obj,'s3':'active','drive':''})

@login_required
def show_gallery(request):
    return redirect('gallery_drive')