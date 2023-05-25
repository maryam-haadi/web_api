from rest_framework.decorators import api_view,permission_classes
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Reserve
from .serializers import Reserve_serializers,show_Reserve_serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def reserve(request):

    reserve1=Reserve_serializers(data=request.data)

    if reserve1.is_valid(raise_exception=True):
        new_reserve=Reserve(user=request.user,phone=reserve1.data['phone'],number=reserve1.data['number'],date=reserve1.data['date'],time=reserve1.data['time'])
        new_reserve.save()
        n_reserve=show_Reserve_serializers(instance=new_reserve)
        return Response({'message':'reserve saved succsesfully','status':'success','reserve':n_reserve.data
            },status=status.HTTP_201_CREATED)

    else:
        return Response(reserve1.errors)




@api_view(["GET"])
@permission_classes([IsAuthenticated])                   #for test
def reserve_list(request):

    res=Reserve.objects.all()
    res_serialize=show_Reserve_serializers(instance=res,many=True)

    return Response(res_serialize.data)



















