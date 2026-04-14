from django.contrib import admin
from django.urls import path

from user import views
from user.views import RegisterView, LoginView, LogoutView, VerifyOTPView, DocumentListUploadView,DeleteSelectedDocumentsView

urlpatterns = [
    # path('',Userview.as_view(),name='index'),
    path("", DocumentListUploadView.as_view(), name="document_list_upload"),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path("documents/delete-selected/", DeleteSelectedDocumentsView.as_view(), name="delete_selected_documents"),

]