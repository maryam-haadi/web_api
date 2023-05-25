from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reserve(models.Model):
    user=models.ForeignKey(User,related_name="reserve",on_delete=models.CASCADE, blank=True)
    phone=models.CharField(max_length=20)
    number=models.IntegerField(blank=False)
    date=models.DateField(auto_now=False,auto_now_add=False)
    time=models.TimeField(auto_now=False,auto_now_add=False)


    def __str__(self):
        return self.phone






















