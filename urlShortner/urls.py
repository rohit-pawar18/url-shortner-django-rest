"""urlShortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from api.views import ShortenerCreateApiView,create_shortner_url_cache, get_shortner_url_cache, get_shortner_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-short-url-cache/',create_shortner_url_cache, name='create_api_cache'),
    path('api/create-short-url/',ShortenerCreateApiView.as_view(),name='create_api'),

    path('api/get-short-url-cache/',get_shortner_url_cache, name='get_api_cache'),
    path('api/get-short-url/',get_shortner_url,name='get_api'),
]


