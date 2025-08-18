from .views import ProductListCreateAPIView
from django.urls import path

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]