from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Reserve
from .serializers import Reserve_serializers


@api_view(["POST"])
def reserve(request):

    reserve1=Reserve_serializers(data=request.data)

    if reserve1.is_valid(raise_exception=True):
        reserve1.save()
        return Response({'message':'reserve saved succsesfully','status':'success','reserve':reserve1.data,
            },status=status.HTTP_201_CREATED)

    else:
        return Response(reserve1.errors)


@api_view(["GET"])
def reserve_list(request):

    res=Reserve.objects.all()
    res_serialize=Reserve_serializers(instance=res,many=True)



    return Response(res_serialize.data)



















