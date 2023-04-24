from django.shortcuts import render
from .models import Blog, Category
from django.utils import timezone
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    """
        List all blogs and categories
    """
    template_name = "blogs/index.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """ Return the list blogs """
        return Blog.objects.all()

    def get_context_data(self):
        context = super().get_context_data()
        context["cates"] = Category.objects.all()
        return context


class DetailView(generic.DetailView):
    """
        get detail of one blog by id
    """
    model = Blog
    template_name = "blogs/detail.html"


class CategoryBlogsView(generic.ListView):
    """
        get all blogs of one category by id
    """
    template_name = "blogs/category.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['blogs'] = Category.objects.get(
            pk=self.kwargs['pk']).blog_set.all()
        return context


# def like(request, blog_id):
#     """
#         like a post
#     """
#     blog = Blog.objects.get(pk=blog_id)
#     like = request.POST['likes']
#     like += 1
#     like.save()
#     context = {
#         "blog": blog
#     }
#     return render(request, "blogs/detail.html", context)
