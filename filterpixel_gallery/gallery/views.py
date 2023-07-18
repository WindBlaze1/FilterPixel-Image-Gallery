from django.shortcuts import render

# Create your views here.

# @login_required
def show_gallery(request):
    return render(request, 'gallery.html')