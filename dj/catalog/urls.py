from django.urls import path

from catalog.views import index, index1

urlpatterns = [
    path('', index),
    path('contacts/', index1)
]