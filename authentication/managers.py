from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from django import forms
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("Email must be set"))
        email =self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email,password,**extra_fields)
        

# def form_validation(data):
#     email = data.get('email','')
#     password = data.get('password','')
#     password2 = data.get('password2','')

#     if not email:
#         raise ValidationError("Email must be set")
#     if not password:
#         raise ValidationError("Password must be set")
#     if not password2:
#         raise ValidationError("Password Confirm must be set")
#     if password != password2:
#         raise ValidationError("Password does not match")
#     return data



