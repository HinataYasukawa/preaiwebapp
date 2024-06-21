from django.urls import path,include
from . import views, processing

app_name = 'file_upload'

urlpatterns = [
    path('', views.file_upload, name='file-upload'),
    path('process/', views.processing, name='processing'),
    path('feedback/', include('feedback.urls')),
    path('processing/<str:filename>/', processing, name='processing'),
]