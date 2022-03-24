"""urlShortner URL Configuration
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


