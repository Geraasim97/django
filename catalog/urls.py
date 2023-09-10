from django.urls import path
from catalog.views import homepage, contacts, index

urlpatterns = [
    path('catalog/', homepage, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('', index ),

]