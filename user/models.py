from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    inpatient =models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    image = models.ImageField(default='avatar.jpg' , upload_to= 'Profile_Images')
    
    def __str__(self):
        return f'{self.inpatient.username}.Profile'
        