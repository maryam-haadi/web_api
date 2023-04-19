from rest_framework import routers, serializers, viewsets
from .models import Food,Comment


class Food_serializers(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'


class Comment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["name","email","message","food"]  








