from rest_framework import serializers
from blogs.models import Blog, Category, User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(source='blog_set', many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'blogs']


class UserSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(source='blog_set', many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'fullname', 'email', 'date_of_birth', 'blogs']
