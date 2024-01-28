# from rest_framework import response
# from django.http import HttpResponse
# import stripe
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, redirect
# from rest_framework.generics import RetrieveAPIView
# from rest_framework import permissions
# # from payment.serializers import ProductSerializer
# from .models import PaymentHistory, Product
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.conf import settings

# # //
# from api.models import ProductModel




# # Create your views here.


# #stripe.api_key=settings.STRIPE_SECRET_KEY

# API_URL="http/locahost:8000"



# # class ProductPreview(RetrieveAPIView):
# #     serializer_class=ProductSerializer
# #     permission_classes=[permissions.AllowAny]
# #     queryset=Product.objects.all()


#  # subject="payment sucessful",
#  #            message=f"thank for your purchase your order is ready.  download url",
#  #            recipient_list=['help.essence@gmail.com'],
#  #            from_email="yashrajsinghji8@gmail.com"


# @csrf_exempt
# def mailSend(request):
# 	# send_mail(
#     #         subject="payment sucessful",
#     #         message=f"thank for your purchase your order is ready.  download url",
#     #         recipient_list=['help.essence@gmail.com'],
#     #         from_email="yashrajsinghji8@gmail.com"
#     #     )
#     # user = ProductModel.objects.all()
# 	subject = f'welcome to GFG world'
# 	message = f'Hi, thank you for registering in geeksforgeeks.'
# 	email_from = 'yash@gmail.com'
# 	recipient_list = ['help.essence@gmail.com']
# 	send_mail( subject, message, email_from, recipient_list )

# 	return HttpResponse('hi')

# class CreateCheckOutSession(APIView):
#     def post(self, request, *args, **kwargs):
#         prod_id=self.kwargs["pk"]
#         try:
#             product=ProductModel.objects.get(id=prod_id)
#             checkout_session = stripe.checkout.Session.create(
#                 line_items=[
#                     {
#                         # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                         'price_data': {
#                             'currency':'usd',
#                              'unit_amount':int(product.price) * 100,
#                              'product_data':{
#                                  'name':product.name,
#                                  'images':[f"{API_URL}/{product.thumbnail}"]

#                              }
#                         },
#                         'quantity': 1,
#                     },
#                 ],
#                 metadata={
#                     "product_id":product.id
#                 },
#                 mode='payment',
#                 success_url=settings.SITE_URL + '?success=true',
#                 cancel_url=settings.SITE_URL + '?canceled=true',
#             )
#             return redirect(checkout_session.url)
#         except Exception as e:
#             return Response({'msg':'something went wrong while creating stripe session','error':str(e)}, status=500)
        



# @csrf_exempt
# def stripe_webhook_view(request):
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     print('hi')
#     try:
#         event = stripe.Webhook.construct_event(
#         payload, sig_header, settings.STRIPE_SECRET_WEBHOOK
#         )
#     except ValueError as e:
#         # Invalid payload
#         return Response(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return Response(status=400)

#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']

#         print(session)
#         customer_email=session['customer_details']['email']
#         prod_id=session['metadata']['product_id']
#         product=ProductModel.objects.get(id=prod_id)
#         #sending confimation mail
#         send_mail(
#             subject="payment sucessful",
#             # message=f"thank for your purchase your order is ready.  download url {product.book_url}",
#             message=f"thank for your purchase your order is ready.  download url {product.slug}",
#             recipient_list=[customer_email],
#             from_email="henry2techgroup@gmail.com"
#         )

#         #creating payment history
#         # user=User.objects.get(email=customer_email) or None

#         PaymentHistory.objects.create(product=product, payment_status=True)
#     # Passed signature verification
#     return HttpResponse(status=200)









# ////////////////////////////////////////////////////////////////////////////////////////////////////////
from django.conf import settings
import stripe
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

from api.models import UserCartModal


# from django.views.generic.base import RedirectView
#             # Create a redirect response to the success URL
#             return RedirectView.as_view(url='success/')(request)


stripe.api_key=settings.STRIPE_SECRET_KEY
API_URL="http/127.0.0.1:8000"
YOUR_DOMAIN = 'https://127.0.0.1:3000'


class CustomAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class CreateCheckoutSession(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):

        user_cart = UserCartModal.objects.filter(user=self.request.user,is_paid=False).first()
        cart_items  = user_cart.cart_items.all()
        item_list = []
        for item in cart_items:
                obj = {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        # 'price': '2000',
                        'price_data':{
                        'currency':'INR',
                         'product_data':{
                        'name':item.name,
                        "description":item.product.smDescription,
                        },
                        'unit_amount':item.price * 100

                        },
                      
                        'quantity': item.quantity,
                    }
                item_list.append(obj)

        try:
            

            checkout_session = stripe.checkout.Session.create(
                line_items=item_list,
                mode='payment',
                payment_method_types=["card"],
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
        except Exception as e:
            return Response(e)
        return Response(checkout_session.url)
        # redirect(checkout_session.url, code=303)



# api_view(['get'])
# @require_http_methods(['GET'])
# def create_checkout_session(request):
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     # 'price': '2000',
#                     'price_data':{
#                     'currency':'usd',
#                      'product_data':{
#                     'name':"Levi's blue jeans"
#                     },
#                     'unit_amount':2000

#                     },
                  
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '?success=true',
#             cancel_url=YOUR_DOMAIN + '?canceled=true',
#         )
#     except Exception as e:
#         return HttpResponse(e)

#     return HttpResponseRedirect(checkout_session.url)
#     # redirect(checkout_session.url, code=303)
