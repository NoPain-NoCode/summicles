from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

class MainAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.all().order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PoliticsListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='정치').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EconomicListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='경제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SocietyListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='사회').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CultureListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='문화').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ForeignListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='국제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DigitalListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='IT/과학').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)