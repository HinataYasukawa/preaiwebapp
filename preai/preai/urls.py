# preai/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('file_upload.urls', namespace='file_upload')),  # namespaceを追加
    path('feedback/', include('feedback.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
