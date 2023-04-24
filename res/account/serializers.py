from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User



class Register_serializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password','email']

























