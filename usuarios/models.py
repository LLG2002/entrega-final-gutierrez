from django.db import models
from django.contrib.auth.models import User
    
class InfoExtra(models.Model):
    avatar= models.ImageField(upload_to='avatars/', null=True, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    localidad= models.CharField(null=True, max_length=15)

