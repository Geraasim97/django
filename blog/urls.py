from django.urls import path

from blog.apps import BlogPostConfig
from blog.views import BlogpostCreateView, BlogpostListView, BlogpostUpdateView, BlogpostDetailView, BlogpostDeleteView

app_name = BlogPostConfig.name

urlpatterns = [
    path('create/', BlogpostCreateView.as_view(), name='create'),
    path('', BlogpostListView.as_view(), name='list'),
    path('view/<int:pk>', BlogpostDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogpostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogpostDeleteView.as_view(), name='delete'),
]