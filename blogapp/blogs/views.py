from django.shortcuts import render
from .models import Blog, Category
from django.utils import timezone
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
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
    model = Blog
    template_name = "blogs/detail.html"


class CategoryBlogsView(generic.ListView):
    template_name = "blogs/category.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['blogs'] = Category.objects.get(
            pk=self.kwargs['pk']).blog_set.all()
        return context

# def list_blog(request):
#     blogs = Blog.objects.all()
#     cates = Category.objects.all()

#     now = timezone.now()
#     context = {
#         "blogs": blogs,
#         "cates": cates,
#         "now": now
#     }
#     return render(request, 'blogs/index.html', context)


# def detail(request, blog_id):
#     blog = Blog.objects.get(pk=blog_id)
#     context = {
#         "blog": blog
#     }
#     return render(request, 'blogs/detail.html', context)


def like(request, blog_id):
    data = request.POST["like"]
    blog = Blog.objects.get(pk=data)
    blog.likes += 1
    blog.save()
    context = {
        "blog": blog
    }
    return render(request, "blogs/detail.html", context)
