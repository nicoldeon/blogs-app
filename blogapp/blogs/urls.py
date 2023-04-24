from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('',  views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('categories/<int:pk>/', views.CategoryBlogsView.as_view(), name="category"),
    # path('<int:pk>/', views.like, name="like"),
]
