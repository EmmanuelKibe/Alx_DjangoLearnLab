from .views import ProductListCreateAPIView, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('', include(router.urls)),
]