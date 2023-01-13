from django.urls import path
from articles.api import views as api_views

urlpatterns = [
    path('all', api_views.CategoriesListView.as_view(), name="category-all"),
    path('create', api_views.CategoryCreate.as_view(), name="category-create"),
    path('detail/<int:pk>', api_views.CategoryDetailAPIView.as_view(), name="category-detail"),
    path('update/<int:pk>', api_views.CategoryUpdateAPIView.as_view(), name="category-update"),
    path('delete/<int:pk>', api_views.CategoryDeleteAPIView.as_view(), name="category-delete"),
]
