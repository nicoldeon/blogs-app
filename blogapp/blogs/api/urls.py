from blogs.api import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    # Blogs

    path('blogs/', views.BlogList.as_view(), name="blogs"),
    path('blogs/<int:pk>', views.DetailBlog.as_view(), name="detail-blog"),

    # Categories
    path('categories/', views.CategoriesList.as_view(), name="categories"),
    path('categories/<int:pk>', views.DetailCategory.as_view(),
         name="detail-category"),
]
