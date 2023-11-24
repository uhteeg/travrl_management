from django.db import models

# Create your models here.
class reguser(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=25)
    def  __str__(self):
        return self.name