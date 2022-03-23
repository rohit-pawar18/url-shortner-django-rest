from rest_framework.serializers import ModelSerializer
from .models import Shortener

class LinkSerializer(ModelSerializer):
    class Meta:
        model=Shortener
        fields=('short_url','long_url')