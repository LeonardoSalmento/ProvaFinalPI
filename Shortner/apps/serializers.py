from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.Serializer):
    texto_original = serializers.CharField()
    texto_encurtado = serializers.CharField(read_only=True)

class SiteDesencurtarSerializer(serializers.Serializer):
    texto_encurtado = serializers.CharField()