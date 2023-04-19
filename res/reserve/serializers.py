from rest_framework import routers, serializers, viewsets
from .models import Reserve


class Reserve_serializers(serializers.ModelSerializer):
    class Meta:
        model=Reserve
        fields='__all__'



















