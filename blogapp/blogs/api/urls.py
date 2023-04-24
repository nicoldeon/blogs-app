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

    # Users
    path('users/', views.UserList.as_view(), name="users"),
    path('users/<int:pk>', views.DetailUser.as_view(), name="detail-user")
]
