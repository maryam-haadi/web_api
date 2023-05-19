from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User




class Register_serializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password','email']



class user_serializers(serializers.ModelSerializer):

    
    class Meta:
        model=User
        fields=['username','email']




class Update_serializers(serializers.Serializer):

    old_username = serializers.CharField(required=True)
    new_username = serializers.CharField(required=True)















