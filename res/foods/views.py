
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Food,Comment,FoodLike,FoodDislike
from .serializers import Food_serializers,Comment_serializers,Show_Comment_serializers,likeSerializer,dislikeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import filters
from rest_framework import generics
import datetime
from django.contrib.auth.models import User
from django.db.models import Q


@api_view(["GET"])
@permission_classes([IsAuthenticated])          #ok
def food_list(request):
    food_list1=Food.objects.all().order_by('-rate')[0:9]
    food_list2=Food_serializers(food_list1,many=True,context={'request':request})
    
    data=food_list2.data
    for f in data:
        if f['photo'].startswith('http'):
            f['photo']=request.build_absolute_uri(f['photo'])

    return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])            #ok
def food_slider(request):

    food_slider1=Food.objects.all().order_by('-id')[:3]
    food_slider2=Food_serializers(food_slider1,many=True,context={'request':request})

    data2=food_slider2.data
    for f1 in data2:
        if f1['photo'].startswith('http'):
            f1['photo']=request.build_absolute_uri(f1['photo'])
    
    return Response(data2)




@api_view(["GET"])
@permission_classes([IsAuthenticated])               #ok
def food_detail(request,f_id):
    try:
        food=Food.objects.get(id=f_id)
    except food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    food2=Food_serializers(instance=food,many=False,context={'request':request})    
    data3=food2.data

    if data3['photo'].startswith('http'):
        data3['photo']=request.build_absolute_uri(data3['photo'])


    return Response(data3)




@api_view(["POST"])
@permission_classes([IsAuthenticated])            #ok
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
@permission_classes([IsAuthenticated])                #ok
def show_comment(request,f_id):

    try:
        food=Food.objects.get(id=f_id)

    except food.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    comment=food.comments

    c_serialize=Show_Comment_serializers(instance=comment,many=True)

    return Response(c_serialize.data)


  




@api_view(["GET"])
@permission_classes([IsAuthenticated])            #ok
def breakfast(request):
    try:
        breakfasts=Food.objects.all().filter(food_type='breakfast')

    except breakfasts.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    breakfast_serialize=Food_serializers(instance=breakfasts,many=True,context={'request':request})
    data4=breakfast_serialize.data

    for f4 in data4:
        if f4['photo'].startswith('http'):
            f4['photo']=request.build_absolute_uri(f4['photo'])

    return Response(data4)



@api_view(["GET"])
@permission_classes([IsAuthenticated])          #ok
def dinner(request):
    try:
        dinner=Food.objects.all().filter(food_type='dinner')

    except dinner.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    dinner_serialize=Food_serializers(instance=dinner,many=True,context={'request':request})
    data5= dinner_serialize.data

    for f5 in data5:
        if f5['photo'].startswith('http'):
            f5['photo']=request.build_absolute_uri(f5['photo'])


    return Response(data5)




@api_view(["GET"])
@permission_classes([IsAuthenticated])            #ok
def lunch(request):
    try:
        lunch=Food.objects.all().filter(food_type='lunch')

    except lunch.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    lunch_serialize=Food_serializers(instance=lunch,many=True,context={'request':request})
    data6= lunch_serialize.data

    for f6 in data6:
        if f6['photo'].startswith('http'):
            f6['photo']=request.build_absolute_uri(f6['photo'])

    return Response(data6)



@api_view(["GET"])
@permission_classes([IsAuthenticated])        #ok
def drink(request):
    try:
        drink=Food.objects.all().filter(food_type='drink')

    except drink.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND) 

    drink_serialize=Food_serializers(instance=drink,many=True,context={'request':request})
    data7= drink_serialize.data

    for f7 in data7:
        if f7['photo'].startswith('http'):
            f7['photo']=request.build_absolute_uri(f7['photo'])

    return Response(data7)






@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_comment(request,c_id):            #vorood check shavad ?

    try:
        comment=Comment.objects.get(id=c_id)
        if comment.user==request.user:
            comment.delete()
            return Response({"message":"comment deleted!!"})
        else:
            return Response({"message":"you dont delete this comment!!"},status=status.HTTP_400_BAD_REQUEST)


    except comment.DoesNotExist:
        if comment is None:
            return Response({"message":"this comment not exist!!"},status=status.HTTP_404_NOT_FOUND) 













class FoodsAPIView(generics.ListCreateAPIView):             #search for food?
    queryset = Food.objects.all()
    serializer_class = Food_serializers
    permission_classes = [IsAdminUser]



class FoodsAPIView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = Food_serializers






@api_view(["GET"])
@permission_classes([IsAuthenticated])             #ok
def like(request,f_id):
    try:

        likeuser = User.objects.get(id=request.user.id)

    except likeuser.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    try:

        likefood = Food.objects.get(id=f_id)

    except likefood.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    check = FoodLike.objects.filter(likeuser=likeuser).filter(likefood=likefood)
    if(check.exists()):

        check.delete()
        if likefood.rate >= 1:
            likefood.rate-=1
            likefood.save()
        return Response({
            "message":"Unliked!!"
            })
    
    new_like = FoodLike.objects.create(likeuser=likeuser, likefood=likefood)
    new_like.save()
    likefood.rate+=1
    likefood.save()
    serializer = likeSerializer(new_like)

    return Response(serializer.data,status=status.HTTP_201_CREATED)







@api_view(["GET"])
@permission_classes([IsAuthenticated])                 #ok
def dislike(request,f_id):
    try:

        dislikeuser = User.objects.get(id=request.user.id)

    except dislikeuser.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    try:

        dislikefood = Food.objects.get(id=f_id)

    except dislikefood.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    check = FoodDislike.objects.filter(dislikeuser=dislikeuser).filter(dislikefood=dislikefood)
    if(check.exists()):
        if dislikefood.negative_rate >= 1:
            dislikefood.negative_rate-=1
            dislikefood.save()
        check.delete()
        return Response({
            "message":"Undisliked!!"
            })
    
    new_dislike = FoodDislike.objects.create(dislikeuser=dislikeuser, dislikefood=dislikefood)
    new_dislike.save()
    
    dislikefood.negative_rate+=1
    dislikefood.save()
    serializer = dislikeSerializer(new_dislike)

    return Response(serializer.data,status=status.HTTP_201_CREATED)






