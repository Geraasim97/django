from django.urls import path

from dj.catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts)
]