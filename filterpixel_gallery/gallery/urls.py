from django.urls import path, include
from gallery import views
from user_auth.views import signup_redirect

urlpatterns = [
    # ('',),
    path('',views.show_gallery,name='gallery'),
    path('gallery/social/signup',signup_redirect,name='signup_redirect'),
    path('',include('allauth.urls')),

]
