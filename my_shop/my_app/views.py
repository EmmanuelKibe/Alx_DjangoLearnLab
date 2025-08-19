# Create your views here.
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from .models import Product, Comment
from rest_framework.response import Response
from .serializers import ProductSerializer, CommentSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        comment = self.get_object()
        comment.flagged = True
        comment.save()
        return Response(
            {"status": "comment flagged"},
            status=status.HTTP_200_OK
        )