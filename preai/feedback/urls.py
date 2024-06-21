from django.urls import path
from .views import result

urlpatterns = [
    path('result/', result, name='result'),
]
