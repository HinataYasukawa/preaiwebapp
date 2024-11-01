from django.urls import path
from . import views  # processingをviewsからインポート

app_name = 'file_upload'  # 名前空間を追加

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('processing/', views.processing, name='processing'),
]