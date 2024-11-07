from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import re

class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        if not phone_number:
            raise ValueError('Phone number is required.')

        # تحقق من طول رقم الهاتف
        if len(phone_number) != 11:
            raise ValueError('Phone number must be 11 digits.')
        
        # تحقق من أن رقم الهاتف يبدأ بـ 010, 011, 012, أو 015
        if not re.match(r'^(010|011|012|015)\d{7}$', phone_number):
            raise ValueError('Phone number must start with 010, 011, 012, or 015.')

        # تحقق من كلمة السر
        if password and len(password) < 8:
            raise ValueError('Password must be at least 8 characters long.')

        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=11, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name']

    def __str__(self):
        return self.email or self.phone_number
