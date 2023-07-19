from django.urls import path, include
from gallery import views
from user_auth.views import signup_redirect

urlpatterns = [
    # ('',),
    path('social/signup',signup_redirect,name='signup_redirect'),
    path('',views.show_gallery,name='gallery'),
    path('drive/',views.show_gallery_drive,name='gallery_drive'),
    path('s3/',views.show_gallery_s3,name='gallery_s3'),
    # path('display_images/',views.fetch_drive_images,name='drive_images'),
    path('',include('allauth.urls')),

]
