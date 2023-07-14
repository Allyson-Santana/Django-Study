
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('upload_img', views.upload_img, name="upload_img"),
]
