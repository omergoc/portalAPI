from rest_framework import status
from rest_framework.response import Response

from articles.models import Article, Categories
from articles.api.serializers import ArticleCreateSerializer, ArticleListSerializer,ArticleUpdateSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.template.defaultfilters import slugify

"""
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema 
import asyncio
from django.http import HttpResponse
from drfasyncview import AsyncRequest, AsyncAPIView
"""

# Category API 
class CategoriesListView(APIView):

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryCreate(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        slug = slugify(request.data['name'].replace('ı', 'i'))
        data_control = Categories.objects.filter(slug=slug)

        if data_control:
                return Response(
            {
                'errors': {
                    'code':404,
                    'message': 'Böyle bir Kategori Bulunmaktadir.'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'errors': {
                    'code':201,
                    'message': 'Başarılı Bir Şekilde Kategori Eklenmiştir.'
                }
            },status=status.HTTP_201_CREATED)

        return Response({
                'errors': {
                    'code':400,
                    'message': 'Geçersiz Parametre İstekleri.'
                }
            },status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        category_instance = get_object_or_404(Categories, pk=pk)
        return category_instance

    def get(self, request, pk):
        category_instance = self.get_object(pk)
        serializer = CategorySerializer(category_instance)
        return Response(serializer.data)



class CategoryUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        category_instance = get_object_or_404(Categories, pk=pk)
        return category_instance

    def put(self, request, pk):
        category_instance = self.get_object(pk)
        slug = slugify(request.data['name'].replace('ı', 'i'))
        data_control = Categories.objects.filter(slug=slug)

        if data_control:
                return Response(
            {
                'errors': {
                    'code':404,
                    'message': 'Böyle bir Kategori Bulunmaktadir.'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
        serializer = CategorySerializer(category_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        category_instance = get_object_or_404(Categories, pk=pk)
        return category_instance

    def delete(self, request, pk):
        category_instance = self.get_object(pk=pk)
        category_instance.delete()
        return Response(
            {
                'errors': {
                    'code': 204,
                    'message': 'Kategori Başarılı Bir Şekilde Silindi.'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )



# Article API
class ArticleListAPIView(APIView):
    def get(self,request):
        articles = Article.objects.filter(available=True)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        slug = slugify(request.data['title'].replace('ı', 'i'))
        data_control = Article.objects.filter(slug=slug)

        if data_control:
                return Response(
            {
                'errors': {
                    'code':404,
                    'message': 'Böyle bir Makale Bulunmaktadir.'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )

        serializer = ArticleCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'errors': {
                    'code':201,
                    'message': 'Başarılı Bir Şekilde Makale Eklenmiştir.'
                }
            },status=status.HTTP_201_CREATED)
        return Response({
                'errors': {
                    'code':400,
                    'message': 'Geçersiz Parametre İstekleri.'
                }
            },status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def get(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleListSerializer(article_instance)
        return Response(serializer.data)


class ArticleUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def put(self, request, pk):
        article_instance = self.get_object(pk=pk)
        slug = slugify(request.data['title'].replace('ı', 'i'))
        data_control = Article.objects.filter(slug=slug)
        if data_control:
            return Response(
            {
                'errors': {
                    'code':404,
                    'message': 'Bu Başlıkta bir Makale Bulunmaktadir.'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )
        serializer = ArticleUpdateSerializer(article_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def delete(self, request, pk):
        article_instance = self.get_object(pk=pk)
        article_instance.delete()
        return Response(
            {
                'errors': {
                    'code':204,
                    'message': 'Makale Başarılı Bir Şekilde Silindi.'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )