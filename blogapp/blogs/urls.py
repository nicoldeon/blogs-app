from django.urls import path
from . import views


urlpatterns = [
    path('',  views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('categories/<int:pk>/', views.CategoryBlogsView.as_view(), name="category"),
    path('<int:blog_id>/', views.like, name="like"),
]
