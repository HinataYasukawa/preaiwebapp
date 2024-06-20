from django.urls import path,include
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('process/', views.processing, name='processing'),
    path('feedback/', include('feedback.urls')),
]