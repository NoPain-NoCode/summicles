from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class MainAPI(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['category', 'title', 'article_date', 'contents', 'newspaper']

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.all().order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PoliticsAPI(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['category', 'title', 'contents', 'newspaper']

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='정치').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EconomicAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='경제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SocietyAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='사회').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CultureAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='문화').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ForeignAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='국제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DigitalAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):  # 어떤 데이터를 가져올 것인지 명시
        return Article.objects.filter(category='IT/과학', category='IT', category='과학').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)