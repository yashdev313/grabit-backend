from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager
# Create your models here.

from .emails import send_otp_mail
from .helpers import generateOTP

OTP_TYPE_CHOICES = (
    ("EMAIL_VERIFY","EMAIL_VERIFY"),
    ("LOGIN_VERIFY_EMAIL","LOGIN_VERIFY_EMAIL"),
    ("RESET_USER_PASSWORD","RESET_USER_PASSWORD"),
)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=20,blank=False,null=False,verbose_name='First Name')
    last_name = models.CharField(max_length=20,blank=False,null=False,verbose_name='Last Name')
    email = models.EmailField(blank=False,null=False,verbose_name='Email Address',unique=True)
    password = models.CharField(max_length=100,blank=False,null=False,verbose_name='Password')
    profile_pic = models.ImageField(verbose_name='Profile Picture',blank=True,null=True)
    email_verified = models.BooleanField(default=False,verbose_name="Email Verified")
    otp = models.CharField(max_length=6,blank=True,null=True,verbose_name="OTP")
    otp_type = models.CharField(max_length=20,blank=True,null=True,choices = OTP_TYPE_CHOICES,verbose_name="Otp Type")
    # reset_password_otp = models.IntegerField(blank=True,null=True,verbose_name="Reset Password OTP")
    created_at = models.DateTimeField(auto_now=True,blank=False,null=False,verbose_name='Created')
    updated_at = models.DateTimeField(auto_now_add=True,blank=False,null=False,verbose_name='Updated')
    # status and
    is_active = models.BooleanField(default=False,verbose_name='Active')
    is_staff = models.BooleanField(default=False,verbose_name='Staff')
    is_superuser = models.BooleanField(default=False,verbose_name='Superuser')

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS=['first_name,last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def send_email(self,email,otp_type):
        otp = generateOTP()
        self.otp = otp
        self.otp_type = otp_type
        send_otp_mail(otp_type,otp,email)
        # self.save()


        # User(email=email,otp_type=OTP_TYPE,otp=OTP)

    

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# from .managers import CustomUserManager
# # Create your models here.

# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     first_name = models.CharField(max_length=20,blank=False,null=False,verbose_name='First Name')
#     last_name = models.CharField(max_length=20,blank=False,null=False,verbose_name='Last Name')
#     email = models.EmailField(blank=False,null=False,verbose_name='Email Address',unique=True)
#     password = models.CharField(max_length=100,blank=False,null=False,verbose_name='Password')
#     profile_pic = models.ImageField(verbose_name='Profile Picture',blank=True,null=True)
#     email_verified = models.BooleanField(default=False,verbose_name="Email Verified")
#     email_verify_otp = models.CharField(max_length=6,blank=True,null=True,verbose_name="Email Verify OTP")
#     reset_password_otp = models.IntegerField(blank=True,null=True,verbose_name="Reset Password OTP")
#     created_at = models.DateTimeField(auto_now=True,blank=False,null=False,verbose_name='Created')
#     updated_at = models.DateTimeField(auto_now_add=True,blank=False,null=False,verbose_name='Updated')
#     # status and
#     is_active = models.BooleanField(default=False,verbose_name='Active')
#     is_staff = models.BooleanField(default=False,verbose_name='Staff')
#     is_superuser = models.BooleanField(default=False,verbose_name='Superuser')

#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS=['first_name,last_name']

#     objects = CustomUserManager()

#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
    
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'

    

