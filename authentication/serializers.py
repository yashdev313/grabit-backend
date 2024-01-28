from rest_framework import serializers
# from .models import CustomUser
from django.contrib.auth.validators import validators
from django.contrib.auth import get_user_model

from django.core.validators import EmailValidator


User = get_user_model()


class SignupUserSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField( max_length=25,required=True)
    class Meta:
        model=User
        fields=['email','password','password_repeat']
        include=['password_repeat']

    
    def validate(self,data):
        # first_name = data['first_name']
        # last_name = data['last_name']
        email = data['email']
        password = data['password']
        password_repeat = data['password_repeat']

        # if not first_name or not last_name or not email or not password:
        #     raise serializers.ValidationError("Required fields can't be empty")
        if password!= password_repeat:
            raise serializers.ValidationError({"error":"Password does not match"})
        # if email=='asdf@gmail.com':
        #     raise serializers.ValidationError("Email Cant be this")
        # if email=='asdf@gmail.com':
        #     raise serializers.ValidationError("Email Cant be this")

        return data


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['email','password']
    
    def validate(self,data):
        email = data['email']
        password = data['password']

        if not email or not password:
            raise serializers.ValidationError("Required fields can't be empty")
        return data

class ResetUserPasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=25,required=True,write_only=True)
    confirm_new_password = serializers.CharField(max_length=25,required=True,write_only=True)

    class Meta:
        model=User
        fields=['email','password','new_password','confirm_new_password']
        extra_kwargs = {'email': {'validators': [EmailValidator,]}}


    def validate(self,data):
        password = data['password']
        new_password = data['new_password']
        confirm_new_password = data['confirm_new_password']

        if new_password != confirm_new_password:
            raise serializers.ValidationError({"error":"Password does not match"})
        return data


class EmailVerifySerializer(serializers.ModelSerializer):
    otp = serializers.CharField(required=True)

    class Meta:
        model=User
        fields=['email','otp']
        extra_kwargs = {'email': {'validators': [EmailValidator,]}}

    def validate(self,data):
        otp = data['otp']
        # if len(otp) != 6:
        #     raise serializers.ValidationError({"error":"Otp should be of 6 digits"})
        return data


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=['email','otp_type']
        extra_kwargs = {'email': {'validators': [EmailValidator,]}}


class OtpVerifySerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(blank=False,null=False,verbose_name='Email Address',unique=True)
    # otp_type = serializers.CharField()
    # otp = 
    class Meta:
        model = User
        fields=['email','otp_type','otp']
        extra_kwargs = {'email': {'validators': [EmailValidator,]}}
    


# class ResetUserPasswordSerializer(serializers.ModelSerializer):
#     old_password = serializers.CharField(max_length=25,required=True)
#     new_password = serializers.CharField(max_length=25,required=True)
#     confirm_new_password = serializers.CharField(max_length=25,required=True)

#     class Meta:
#         model=CustomUser
#         fields=['email','old_password','new_password','confirm_new_password']


#     def validate(self,data):
#         old_password = data['old_password']
#         new_password = data['new_password']
#         confirm_new_password = data['confirm_new_password']

#         if new_password != confirm_new_password:
#             raise serializers.ValidationError({"error":"Password does not match"})
#         return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','profile_pic',)


# 

# 

# from rest_framework import serializers    

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension


class UserProfileSerializer(serializers.ModelSerializer):
    # profile_pic= Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = User
        fields = ('profile_pic',)