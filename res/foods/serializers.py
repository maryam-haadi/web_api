from rest_framework import routers, serializers, viewsets
from .models import Food,Comment


class Food_serializers(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'


class Comment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["food","message"]  



class Show_Comment_serializers(serializers.ModelSerializer):
        
    class Meta:
        model=Comment
        fields=["user","message","food"]  




