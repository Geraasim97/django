from django.urls import path
from catalog.views import index, index2


urlpatterns = [
    path('', index),
    path('about', index2)
]