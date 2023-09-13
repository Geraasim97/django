from django.urls import path
from catalog.apps import MainConfig

from catalog.views import index, product, contact

app_name = MainConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contact, name='contact'),
    path('<int:pk> /product/', product, name='product')
]