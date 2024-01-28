from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework import authentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password

from django.views.decorators.csrf import csrf_exempt

from .serializers import SignupUserSerializer,LoginUserSerializer,ResetUserPasswordSerializer, EmailVerifySerializer, EmailSerializer, OtpVerifySerializer, UserSerializer, UserProfileSerializer
from .models import CustomUser as User
from .helpers import generateOTP

from .emails import send_otp_mail

from django.utils.decorators import method_decorator

from rest_framework import  generics



# 

class CustomAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

# 



class SignupUser(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]
    
    def post(self,request,*args,**kwargs):
        data=request.data
        serializer = SignupUserSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            OTP = generateOTP()
            OTP_TYPE = "EMAIL_VERIFY"
            user = User(email=email)
            user.set_password(password)
            user.send_email(email,OTP_TYPE)
            user.save()
            return Response({'message':'Email has been sent to your email address'},status=status.HTTP_201_CREATED,headers={"success":"true"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})

        
class LoginUser(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]
    
    def post(self,request):
        data=request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request,email=email,password=password)
            if(user):
                login(request,user)
                return Response({"message":"User logged in"},status=status.HTTP_200_OK,headers={"success":"true"})
            return Response({"message":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED,headers={"success":"false"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message":"Logout successful"},status=status.HTTP_200_OK,headers={"success":"true"})
        return Response({"message":"You are not logged in"},status=status.HTTP_401_UNAUTHORIZED,headers={"success":"false"})
        

class ResetUserPassword(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        data = request.data
        serializer = ResetUserPasswordSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            old_password = serializer.validated_data['password']
            new_password = serializer.validated_data['new_password']
            user = authenticate(request,email=email,password=old_password)
            # print(user)
            OTP_TYPE = "RESET_USER_PASSWORD"
            if(user):
                password_same = check_password(new_password,user.password)
                if password_same :
                    return Response({"message":"New password should not be same as old password"},status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})
                user.set_password(new_password)
                user.save()
                return Response({"message":"Password has been changed."},status=status.HTTP_200_OK,headers={"success":"true"})
            return Response({"message":"Invalid credentials."},status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})


class OtpVerify(APIView):
    # authentication_classes=[authentication.SessionAuthentication]
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        data = request.data
        serializer = OtpVerifySerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            otp_type = serializer.validated_data['otp_type']
            user = User.objects.filter(email=email,otp_type=otp_type,otp=otp).first()
            if(user):
                if otp_type == "EMAIL_VERIFY":
                    user.email_verified=True
                    user.is_active = True
                    user.otp_type=None
                    user.otp=None
                    user.save()
                    return Response({"message":"Your email is verified, your account has been activated"},status=status.HTTP_200_OK,headers={"success":"true"})
            return Response({"message":"Otp is invalid"},status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ResendOtp(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        data = request.data
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            OTP_TYPE = "EMAIL_VERIFY"
            user = User.objects.filter(email=email).first()
            if user:
                user.send_email(email,OTP_TYPE)
                user.save()
                return Response({"message":"Otp has been sent."},status=status.HTTP_200_OK,headers={"success":"true"})
            return Response({"message":"User with this email does not exist"},status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST,headers={"success":"false"})


class CheckUser(APIView):
    authentication_classes =[CustomAuthentication]
    permissions = [permissions.IsAuthenticated]
    def post(self,request):
        # print(request.user.email)
        return Response(request.user.email)


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class=UserSerializer
    authentication_classes=[CustomAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            email = self.request.user.email
            user = User.objects.filter(email = email).first()
            return user
        Response({
            "first_name": "",
            "last_name": "",
            "email": "",
            "profile_pic": None
        })

    def get_object(self):
        # obj = get_object_or_404(queryset, user=self.request.user)
        # serializer.is_valid(raise_exception=True)
        # return serializer.validated_data
        return self.get_queryset()

    # def update(self,request):
    #     return Response("User")


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User
    serializer_class = UserProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[CustomAuthentication]

    def get_queryset(self):
        email = self.request.user.email
        user = User.objects.filter(email = email).first()
        return user

    def get_object(self):
        return self.get_queryset()


class CheckUserIsAuthenticated(APIView):
    authentication_classes=[CustomAuthentication]
    permission_classes=[permissions.AllowAny]

    def get(self,request):
        # print(self.request.user)
        if(self.request.user.is_authenticated):
            return Response(True)
        return Response(False)