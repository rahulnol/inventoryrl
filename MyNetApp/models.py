from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser



class MyUser(AbstractUser):
    phone_number = models.IntegerField(unique=True,blank=True,null=True)
    city = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'







