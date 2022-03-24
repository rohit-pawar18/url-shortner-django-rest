from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.cache import cache

from .serializer import LinkSerializer
from .models import Shortener, create_random_code



class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response({"short_url": f"{settings.HOST}{instance.short_url}"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_shortner_url(request):
    
    short_url = request.GET.get('short_url')
    if not short_url:
        return Response({"ERROR": f"Please provide short url"},status=status.HTTP_404_NOT_FOUND)
    code = short_url.split(settings.HOST)[1]
    try:
        obj = Shortener.objects.get(short_url=code)
        return HttpResponseRedirect(obj.long_url)
    except:
        return Response({"ERROR": "No url found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create_shortner_url_cache(request):
    random_code = create_random_code()
    cache.set(random_code,request.data.get('long_url'))
    return Response({"short_url": f"{settings.HOST}{random_code}"},status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_shortner_url_cache(request):
    short_url = request.GET.get('short_url')
    if not short_url:
        return Response({"ERROR": f"Please provide short url"},status=status.HTTP_404_NOT_FOUND)
    code = short_url.split(settings.HOST)[1]
    return HttpResponseRedirect(cache.get(code))
