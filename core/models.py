from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    address_text = models.CharField(max_length=255,null=True,blank=True)
    address = models.BinaryField(null=True,blank=True)
    address1 = models.BinaryField(null=True,blank=True)
    address2 = models.BinaryField(null=True,blank=True)
    contact_no = models.CharField(max_length=255,null=True,blank=True)
    encrypted_pii = models.BinaryField(null=True,blank=True)

    def __str__(self):
        return self.email