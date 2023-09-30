from django.urls import path
from catalog.apps import MainConfig
from catalog.views import ProductDetailView, ProductUpdateView, ProductDeleteView
from catalog.views import IndexView, ProductListView, ContactView, ProductCreateView
from django.views.decorators.cache import cache_page

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]