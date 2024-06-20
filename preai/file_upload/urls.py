from django.urls import path
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('upload/', views.fileupload, name='fileupload'),
    path('process/', views.processing, name='processing'),
]