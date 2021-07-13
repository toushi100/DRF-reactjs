from blog.models import Category, Post
from rest_framework import fields, serializers
from blog.models import Post,Category

class PostSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','category','author','excerpt','content','status')

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')