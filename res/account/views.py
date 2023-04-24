
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .serializers import Register_serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import json
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





@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = request.data
        email = reqBody['email']
        username = reqBody['username']
        print(email)
        password = reqBody['password']
        print(password)
        try:

            Account = User.objects.get(username=username,email=email)
            print(Account.password)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

           
        token = Token.objects.get_or_create(user=Account)[0].key
        print(token)
        if password != Account.password:
            raise ValidationError({"message": "Incorrect Login credentials"})

        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.email

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_user(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')










