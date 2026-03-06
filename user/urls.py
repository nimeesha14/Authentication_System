from django.contrib import admin
from django.urls import path

from user import views
from user.views import RegisterView, LoginView, LogoutView, Userview

urlpatterns = [
    path('',Userview.as_view(),name='index'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]