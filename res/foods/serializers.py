from rest_framework import routers, serializers, viewsets
from .models import Food,Comment,FoodLike,FoodDislike


class Food_serializers(serializers.ModelSerializer):
    photo=serializers.SerializerMethodField()
    class Meta:
        model=Food
        fields=['id','name','description','rate','negative_rate','price','time','photo','food_type']

    def get_photo(self,obj):
        if obj.photo:
            request=self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.photo.url)
        return None



class Comment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["message"]  



class Show_Comment_serializers(serializers.ModelSerializer):
        
    class Meta:
        model=Comment
        fields=["id","user","message","date"]  


class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodLike
        fields = ['likeuser']        

class dislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDislike
        fields = ['dislikeuser']    


