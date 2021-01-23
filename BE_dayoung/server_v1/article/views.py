from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, mixins

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticleListAPI(ListView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
