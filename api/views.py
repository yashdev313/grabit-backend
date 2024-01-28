from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, DestroyAPIView, CreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins

from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponseRedirect

from .models import ProductModel, CategoryModel,CartItemsModal,UserCartModal,ColorVariantModel,SizeVariantModel,SavedItemsModal,UserSavedModal,AddressesModel,UserAddressesModel,LandingSlideModal,CategoryClassModel
from .serializers import ProductSerializer, CategorySerializer,CartItemsSerializer, SavedItemsSerializer,AddressesSerializer,UserAddressesSerializer,LandingSlideSerializer,CategoryClassSerializer, UserCartSerializer
from rest_framework.views import APIView
# Create your views here.
import json
import io
from rest_framework.parsers import JSONParser

# filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomFilter
from io import BytesIO


import urllib.parse
# @api_view(['get'])
# def homeView(request):
#     return Response({"Hello World"})

# def productRedirectView(request):
#     return HttpResponseRedirect('product')

# from django.utils.decorators import method_decorator

class CustomAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening







class ProductView(ListAPIView):
    # model = ProductModel
    # queryset = ProductModel.objects.filter(status='Publish')
    serializer_class = ProductSerializer
    permission_classes=[AllowAny]
    filter_backends =[filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name','category__name']
    filterset_class = CustomFilter
    # filterset_fields = ['category','productmodel__price']

    # def get(self,request):
    #     response = Response('hi',headers={'Location': urllib.parse.quote('/cart')})
    #     # response['Location'] = urllib.parse.quote('/cart')
    #     return response


    def get_queryset(self):
        return ProductModel.objects.filter(status='Publish')



class LandingSlideView(ListAPIView):
    queryset=LandingSlideModal.objects.all()
    serializer_class=LandingSlideSerializer
    permission_classes=[AllowAny]


class ProductDetailView(RetrieveAPIView):
    model = ProductModel
    serializer_class = ProductSerializer
    lookup_field='slug'
    lookup_url_kwarg='slug'
    permission_classes=[AllowAny]
    queryset = ProductModel.objects.all()


class SavedItemsView(ListCreateAPIView):
    model=SavedItemsModal
    serializer_class =SavedItemsSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        user_saved_products,created = UserSavedModal.objects.get_or_create(user=self.request.user)
        return user_saved_products.saved_items.all()

    def post(self,request):
        product_id =request.data.get('product','')
        user,created = UserSavedModal.objects.get_or_create(user = request.user)
        product = ProductModel.objects.get(id=product_id)
        saveditems = SavedItemsModal.objects.create(user=user,product=product)
        return Response("Product is saved.")


class CartItemsView(ListCreateAPIView):
    model = CartItemsModal
    serializer_class = CartItemsSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[CustomAuthentication]
    # authentication_classes=[authentication.SessionAuthentication]

    def get_queryset(self):
        user_cart,created = UserCartModal.objects.get_or_create(user=self.request.user,is_paid=False)
        return user_cart.cart_items.all()

    def post(self,request):
        product_id = request.data.get('id','')
        color = request.data.get('color','')
        size = request.data.get('size','')
        quantity = request.data.get('quantity',1)

        user,created = UserCartModal.objects.get_or_create(user = request.user,is_paid=False)

        if product_id:
            product = ProductModel.objects.filter(id=product_id).first()
            if product:
                cart_item,created = CartItemsModal.objects.get_or_create(user=user,product=product,quantity=quantity)
                if color:
                    color_variant_instance = ColorVariantModel.objects.get(id=color)
                    cart_item.color_variant = color_variant_instance
                if size:
                    size_variant_instance = SizeVariantModel.objects.get(id=size)
                    cart_item.size_variant = size_variant_instance
                cart_item.save()
            return Response(True)
        return Response(False,status.HTTP_400_BAD_REQUEST)


class UserSelectedAddressView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[CustomAuthentication]

    def get(self,request):
        user_address,created = UserAddressesModel.objects.get_or_create(user=request.user)
        if user_address.delievery_address:
            address = user_address.addresses.filter(id=user_address.delievery_address.id).first()
            serializer=UserAddressesSerializer(user_address)
            return Response(serializer.data)
        return Response("No address saved.")


    def put(self,request):
        address_id = request.data.get('delievery_address','')
        user_address,created = UserAddressesModel.objects.get_or_create(user=request.user)
        address = user_address.addresses.filter(id=address_id).first()
        if(address):
            user_address.delievery_address = address
            user_address.save()
            return Response('Delievery address has been updated.')
        return Response('Address does not exist.',status=status.HTTP_400_BAD_REQUEST)


class AddressesView(ListCreateAPIView):
    model=AddressesModel
    serializer_class =AddressesSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_address,created = UserAddressesModel.objects.get_or_create(user=self.request.user)
        return user_address.addresses.all()

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']
            mobile_number = serializer.validated_data['mobile_number']
            alternate_mobile_number = serializer.validated_data['alternate_mobile_number']
            email = serializer.validated_data['email']
            street = serializer.validated_data['street']
            landmark = serializer.validated_data['landmark']
            city = serializer.validated_data['city']
            state = serializer.validated_data['state']
            country = serializer.validated_data['country']
            pincode = serializer.validated_data['pincode']
            user_address,created = UserAddressesModel.objects.get_or_create(user = request.user)
            address,created = AddressesModel.objects.get_or_create(user=user_address,first_name=first_name,last_name=last_name,mobile_number=mobile_number,alternate_mobile_number=alternate_mobile_number,email=email,street=street,landmark=landmark,city=city,state=state,country=country,pincode=pincode)

            # it may be 1 st time when address id added, we are using user_address.addresses.count() may be zero even after updating because we are using previous user_address and after updating address, so please check it carefully 
            if user_address.addresses.count() == 1:
                user_address.delievery_address = address
                user_address.save()
            return Response("User address updated")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyAddressView(RetrieveUpdateDestroyAPIView):
    queryset = AddressesModel
    serializer_class=AddressesSerializer
    lookup_url_kwarg = 'id'
    lookup_field='id'
    permission_classes=[IsAuthenticated]
    authentication_classes=[CustomAuthentication]


class UserCartView(RetrieveAPIView):
    queryset=UserCartModal
    serializer_class = UserCartSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]

    def get_object(self):
        obj = self.queryset.objects.filter(user=self.request.user,is_paid=False).first()
        return obj


class CartItemsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset=CartItemsModal
    serializer_class=CartItemsSerializer
    lookup_url_kwarg='id'
    lookup_field='id'
    authentication_classes=[CustomAuthentication]
    permission_classes =[IsAuthenticated]


class CategoryView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[AllowAny]


class CategoryClassView(ListAPIView):
    queryset=CategoryClassModel.objects.all()
    serializer_class = CategoryClassSerializer
    permission_classes=[AllowAny]
    # filter_backends = (filters.OrderingFilter)
    filter_backends =[filters.OrderingFilter]


class CategoryDetailView(RetrieveAPIView):
    pass


class ProductFilteredByCategory(ListAPIView):
    serializer_class=ProductSerializer
    permission_classes=[AllowAny]

    def get_queryset(self):
        return ProductModel.objects.filter(category__name=self.kwargs['category'])
