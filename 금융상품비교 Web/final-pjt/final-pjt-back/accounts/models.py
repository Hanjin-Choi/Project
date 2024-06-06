from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    pass

class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField()
    asset = models.IntegerField()
    salary = models.IntegerField()
    ivst_taste = models.CharField(max_length=10) ## selectbox??
    prdt_list = models.TextField()
    favorite = models.CharField(max_length=20)
