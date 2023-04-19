from django.db import models

# Create your models here.



class Food(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=50)
    rate=models.IntegerField(default=0)
    price=models.IntegerField(blank=False)
    time=models.IntegerField(blank=False)
    photo=models.ImageField(upload_to='foods/',blank=False)
    food_type=models.CharField(max_length=50,blank=False,default=None)

    def __str__(self):
        return self.name

class Comment(models.Model):
    food=models.ForeignKey("Food",verbose_name=("food"),related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    message=models.TextField()
    date=models.DateField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.email













