from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from blog.models import Post,Category
from .serializers import PostSerialzer,CategorySerialzer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postObjects.all()
    serializer_class = PostSerialzer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.postObjects.all()
    serializer_class = PostSerialzer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer