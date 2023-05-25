from rest_framework import routers, serializers, viewsets
from .models import Reserve


class Reserve_serializers(serializers.ModelSerializer):
    class Meta:
        model=Reserve
        fields=['phone','number','date','time']




class show_Reserve_serializers(serializers.ModelSerializer):
    class Meta:
        model=Reserve
        fields=['user','phone','number','date','time']














