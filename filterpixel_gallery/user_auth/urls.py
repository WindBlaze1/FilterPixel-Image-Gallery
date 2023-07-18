from django.urls import path
from user_auth import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.loginRequest, name='login'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logoutRequest, name='logout'),
]
