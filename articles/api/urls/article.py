from django.urls import path
from articles.api import views as api_views

urlpatterns = [
    path('all', api_views.ArticleListAPIView.as_view(), name="article-all"),
    path('create', api_views.ArticleCreateAPIView.as_view(), name="article-create"),
    path('detail/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name="article-detail"),
    path('update/<int:pk>', api_views.ArticleUpdateAPIView.as_view(), name="article-update"),
    path('delete/<int:pk>', api_views.ArticleDeleteAPIView.as_view(), name="article-delete"),
]
