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
        cate.delete()
        return Response(status=204)

# @api_view(['GET'])
# def api_categories_view(request):
#     if request.method == "GET":
#         cates = Category.objects.all()
#         serializer = CategorySerializer(cates, many=True)
#         return Response(serializer.data)


# @api_view(['POST'])
# def api_create_category(request):
#     cate = Category()
#     if request.method == "POST":
#         serializer = CategorySerializer(cate, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['GET'])
# def api_detail_category(request, pk):
#     try:
#         cate = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = CategorySerializer(cate)
#         return Response(serializer.data)


# @api_view(['DELETE'])
# def api_delete_category(request, pk):
#     try:
#         cate = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=404)

#     if request.method == "DELETE":
#         operation = cate.delete()
#         data = {}
#         if operation:
#             # if it valid you change the serializer
#             data["success"] = "delete sucessful"
#         else:
#             data["failed"] = "delete failed"
#         return Response(data=data)


# @api_view(['PUT'])
# def api_update_category(request, pk):
#     try:
#         cate = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response(status=404)

#     if request.method == "PUT":
#         serializer = CategorySerializer(cate, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             # if it valid you change the serializer
#             serializer.save()
#             data["success"] = "update sucessful"
#             return Response(data=data)
#         return Response(serializer.errors, status=400)


# Blog
class BlogList(APIView):
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
        blog.delete()
        return Response(status=200)

# @api_view(['GET'])
# def api_blog_view(request):
#     if request.method == "GET":
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)


# @api_view(['GET'])
# def api_detail_blog(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)


# @api_view(['PUT'])
# def api_update_blog(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=404)

#     if request.method == "PUT":
#         serializer = BlogSerializer(blog, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             # if it valid you change the serializer
#             serializer.save()
#             data["success"] = "update sucessful"
#             return Response(data=data)
#         return Response(serializer.errors, status=400)


# @api_view(['DELETE'])
# def api_delete_blog(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=404)

#     if request.method == "DELETE":
#         operation = blog.delete()
#         data = {}
#         if operation:
#             # if it valid you change the serializer
#             data["success"] = "delete sucessful"
#         else:
#             data["failed"] = "delete failed"
#         return Response(data=data)


# # require author to be authenticated to be created a post
# @api_view(['POST'])
# def api_create_blog(request):
#     blog = Blog()
#     if request.method == "POST":
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
