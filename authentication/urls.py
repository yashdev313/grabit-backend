from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns = [
    path('signup/', views.SignupUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.LogoutUser.as_view()),
    path('reset-password/', views.ResetUserPassword.as_view()),
    path('verify-otp/', views.OtpVerify.as_view()),
    path('send-otp/', views.ResendOtp.as_view()),
    path('user-details/', views.UserDetailView.as_view()),
    path('check-user/', views.CheckUserIsAuthenticated.as_view()),
    path('user-profile-update/', views.UserProfileView.as_view()),

    # 
    # path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    
]
