from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
# from .views import CreateCheckOutSession, stripe_webhook_view,mailSend
from . import views



urlpatterns = [
    # path('payment/'include(payment.urls))
    # path('payment/'include(payment.urls))
    # path('payment/'include(payment.urls))
    #path('create-checkout-session/<pk>/', csrf_exempt(CreateCheckOutSession.as_view()), name='checkout_session'),
    # path('stripe-webhook/', stripe_webhook_view, name='stripe-webhook'),
    path('create-checkout-session/',views.CreateCheckoutSession.as_view(), name='create-checkout-session'),


    # 
    #path('send-mail',mailSend)
    # 


]







# from django.urls import path
# from .views import ProductPreview, CreateCheckOutSession, stripe_webhook_view
# from django.views.decorators.csrf import csrf_exempt

# urlpatterns=[
#     path('product/<int:pk>/', ProductPreview.as_view(), name="product"),
#     # path('payment-with-stripe/', CustomPaymentEndpoint.as_view())
#     ]