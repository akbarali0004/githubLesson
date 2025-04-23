from django.urls import path
from .views import postReader


urlpatterns = [
    path("", postReader, name='posts'),
]