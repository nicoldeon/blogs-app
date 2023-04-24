from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from blogs.models import Blog, Category
from blogs.api.serializers import BlogSerializer, CategorySerializer


# Category
class CategoriesList(APIView):
    """
        List all categories, create new categories
    """

    def get(self, request, format=None):
        cates = Category.objects.all()
        serializer = CategorySerializer(cates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DetailCategory(APIView):
    """
        get detail category by id, delete and update that category
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Response(status=404)

    def get(self, request, pk, format=None):
        cate = self.get_object(pk)
        serializer = CategorySerializer(cate)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cate = self.get_object(pk)
        serializer = CategorySerializer(cate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        cate = self.get_object(pk)
        data = {}
        if cate.delete():
            data['delete'] = "Delete successful"
        return Response(data, status=204)


# Blog
class BlogList(APIView):
    """
        list all blogs, and create new blog
    """

    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=404)


class DetailBlog(APIView):
    """
        get detail of one blog by id, delelete and update that blog
    """

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            Response(status=404)

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        data = {}
        if blog.delete():
            data['delete'] = "Delete successful"
        return Response(data, status=200)
