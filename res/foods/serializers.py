from rest_framework import routers, serializers, viewsets
from .models import Food,Comment,FoodLike,FoodDislike


class Food_serializers(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'


class Comment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["message"]  



class Show_Comment_serializers(serializers.ModelSerializer):
        
    class Meta:
        model=Comment
        fields=["user","message","date"]  


class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLike
        fields = ['likeuser']        

class dislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDislike
        fields = ['dislikeuser']    


