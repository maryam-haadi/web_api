
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Food,Comment,FoodLike
from .serializers import Food_serializers,Comment_serializers,Show_Comment_serializers,likeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import filters
from rest_framework import generics
import datetime
from django.contrib.auth.models import User
from django.db.models import Q

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def food_list(request):
    food_list1=Food.objects.all().order_by('rate')[2:4]
    food_list2=Food_serializers(food_list1,many=True)
    
    return Response({'food_list':food_list2.data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def food_slider(request):

    food_slider1=Food.objects.all().order_by('id')[:3]
    food_slider2=Food_serializers(food_slider1,many=True)
    
    return Response({'food_slider':food_slider2.data})




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def food_detail(request,f_id):
    try:
        food=Food.objects.get(id=f_id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    food2=Food_serializers(instance=food,many=False)    

    return Response({'detail_food':food2.data})




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_comment(request,f_id):
    try:
        food=Food.objects.get(id=f_id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    new_comment=Comment_serializers(data=request.data)
    if new_comment.is_valid(raise_exception=True):

        date1=datetime.datetime.now()
        new_comment2=Comment(food=food,user=request.user,message=new_comment.data["message"],date=date1)

        new_comment2.save()
        n_comment=Show_Comment_serializers(instance=new_comment2)
        return Response({'message':'comment saved succsesfully','status':'success','comment_for_food':food.id,'comment':n_comment.data,
        },status=status.HTTP_201_CREATED)

    return Response(new_comment.errors)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_comment(request,f_id):

    try:
        food=Food.objects.get(id=f_id)

    except food.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    comment=food.comments

    c_serialize=Show_Comment_serializers(instance=comment,many=True)

    return Response({"comments":c_serialize.data})


  




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def breakfast(request):
    try:
        breakfasts=Food.objects.all().filter(food_type='breakfast')

    except breakfasts.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    breakfast_serialize=Food_serializers(instance=breakfasts,many=True)

    return Response(breakfast_serialize.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dinner(request):
    try:
        dinner=Food.objects.all().filter(food_type='dinner')

    except dinner.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    dinner_serialize=Food_serializers(instance=dinner,many=True)

    return Response(dinner_serialize.data)




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def lunch(request):
    try:
        lunch=Food.objects.all().filter(food_type='lunch')

    except lunch.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    lunch_serialize=Food_serializers(instance=lunch,many=True)

    return Response(lunch_serialize.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def drink(request):
    try:
        drink=Food.objects.all().filter(food_type='drink')

    except drink.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    drink_serialize=Food_serializers(instance=drink,many=True)

    return Response(drink_serialize.data)






@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_comment(request,c_id):         

    try:
        comment=Comment.objects.get(id=c_id)
        if comment.user==request.user:
            comment.delete()
            return Response({"message":"comment deleted!!"})
        else:
            return Response({"message":"you dont delete this comment!!"},status=status.HTTP_400_BAD_REQUEST)

    except comment.DoesNotExist:
        return Response({"message":"this comment not exist!!"},status=status.HTTP_404_NOT_FOUND) 













class FoodsAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = Food_serializers
    permission_classes = [IsAdminUser]



class FoodsAPIView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = Food_serializers



def like(request,f_id):
    try:

        likeuser = User.objects.get(id=request.user.id)

    except likeuser.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    likefood = Food.objects.filter(id=f_id)
    check = FoodLike.objects.filter(Q(likeuser__name__contains=likeuser) & Q(likefood__name__contains=likefood ))
    if(check.exists()):
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message":"Already Liked"
            })
    new_like = FoodLike.objects.create(likeusers=likeuser, likepost=likefood)
    new_like.save()
    likefood.rate+=1
    likefood.save()
    serializer = likeSerializer(new_like)
    return Response(serializer.data,status=status.HTTP_201_CREATED)








