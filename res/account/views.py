
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import Register_serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from django.core.exceptions import ValidationError
# Create your views here.



@api_view(["POST"])
@permission_classes([AllowAny])
def Register(request):
    try:
        data = dict()
        serializer = Register_serializers(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["username"] = account.username
            data["password"] = account.password
            data["email"] = account.email
            data["token"] = token

        else:
            data = serializer.errors


        return Response(data)
    
    except IntegrityError as e:
        account=User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})




@api_view(["GET"])
def user_list(request):
    users=User.objects.all()
    user_serializer=Register_serializers(users,many=True)
    return Response(user_serializer.data)




















