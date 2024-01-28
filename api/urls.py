from django.contrib import admin
from django.urls import path, include
# from .views import ProductView, ProductDetailView, CategoryView, CategoryDetailView,UserCartView,CartItemsView,CartItemsDeleteView,SavedItemsView,AddressesView,UserSelectedAddressView,LandingSlideView,ProductFilteredByCategory,RetrieveUpdateAddressView,CategoryClassView
from . import views
# productRedirectView



# accounts/urls.py
from . import views

# urlpatterns = [
#     path('login', UserLoginView.as_view(), name="api-auth-login"),
#     path('logout', UserLogoutView.as_view(), name="api-auth-logout"),
#     path('register/', UserRegisterView.as_view(), name="api-auth-register"),
# ]




urlpatterns = [
    # path('', productRedirectView, name='redirect_view'),
    path('', views.ProductView.as_view(), name='home'),
    path('product/<str:slug>', views.ProductDetailView.as_view(), name='home'),
    path('saved/', views.SavedItemsView.as_view(), name='home'),
    # path('saved/<str:product>', SavedDeleteView.as_view(), name='home'),
    path('user-cart/', views.UserCartView.as_view(), name='home'),
    path('cart/', views.CartItemsView.as_view(), name='home'),
    path('cart/<str:id>', views.CartItemsRetrieveUpdateDestroyView.as_view(), name='home'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<str:category>', views.ProductFilteredByCategory.as_view(), name='category'),
    path('address/', views.AddressesView.as_view(), name='address'),
    path('get-user-selected-address/', views.UserSelectedAddressView.as_view(), name='address'),
    path('get-landing-slides/',views.LandingSlideView.as_view(),name='landing-slides'),
    path('address/<str:id>/',views.RetrieveUpdateDestroyAddressView.as_view(),name='landing-slides'),
    path('get-category-class',views.CategoryClassView.as_view(),name='category_class'),
    path('saved-products',views.SavedItemsView.as_view(),name='category_class')

]
