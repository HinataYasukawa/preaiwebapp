# feedback/urls.py
from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('result/', views.result, name='result'),
]
