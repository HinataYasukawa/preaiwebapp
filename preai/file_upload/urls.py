from django.urls import path
from . import views  # processingをviewsからインポート

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('processing/<str:filename>/', views.processing, name='processing'),
]
