"""summicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import MainAPI, PoliticsAPI, EconomicAPI, SocietyAPI, CultureAPI, ForeignAPI, DigitalAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', MainAPI.as_view()),
    path('politics/', PoliticsAPI.as_view()),
    path('economic/', EconomicAPI.as_view()),
    path('society/', SocietyAPI.as_view()),
    path('culture/', CultureAPI.as_view()),
    path('foreign/', ForeignAPI.as_view()),
    path('digital/', DigitalAPI.as_view()),
]
