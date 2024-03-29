from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Food(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=50)
    rate=models.IntegerField(default=0)
    negative_rate=models.IntegerField(default=0)
    price=models.IntegerField(blank=False)
    time=models.IntegerField(blank=False)
    photo=models.ImageField(upload_to='foods/',blank=False)
    food_type=models.CharField(max_length=50,blank=False,default=None)

    def __str__(self):
        return self.name


class Comment(models.Model):
    food=models.ForeignKey(Food,verbose_name=("food"),related_name="comments",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="comment",on_delete=models.CASCADE, blank=True)
    message=models.TextField()
    date=models.DateField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.food.name

class FoodLike(models.Model):
    likeuser=models.ForeignKey(User,related_name="like",on_delete=models.CASCADE)
    likefood=models.ForeignKey(Food,related_name="likes",on_delete=models.CASCADE,null=True)


class FoodDislike(models.Model):
    dislikeuser=models.ForeignKey(User,related_name="Dislike",on_delete=models.CASCADE)
    dislikefood=models.ForeignKey(Food,related_name="Dislikes",on_delete=models.CASCADE,null=True)








