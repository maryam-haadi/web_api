from django.db import models

# Create your models here.

class Reserve(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=300)
    phone=models.CharField(max_length=20)
    number=models.IntegerField(blank=False)
    date=models.DateField(auto_now=False,auto_now_add=False)
    time=models.TimeField(auto_now=False,auto_now_add=False)


    def __str__(self):
        return self.email






















