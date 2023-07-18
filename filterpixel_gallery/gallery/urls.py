from django.urls import path, include
from gallery import views
from user_auth.views import signup_redirect

urlpatterns = [
    # ('',),
    path('',views.show_gallery,name='gallery'),
    # path('display_images/',views.fetch_drive_images,name='drive_images'),
    path('gallery/social/signup',signup_redirect,name='signup_redirect'),
    path('',include('allauth.urls')),

]
