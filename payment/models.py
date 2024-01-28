# # Create your models here.

# from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from api.models import BaseModel
# import uuid


# class BaseModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# #  User Payments
# class UserPaymentModel(BaseModel):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_payments')
#     # product = models.ForeignKey('ProductModel',on_delete=models.SET_NULL,related_name='user_payments')// if prouct is deleted why to 
#     payment_bool = models.BooleanField(default=False)
#     stripe_checkout_id = models.CharField(max_length=500)


#     class Meta:
#         verbose_name= "UserPaymentModel"
#         verbose_name_plural = "UserPaymentModel"



#     def __str__(self):
#         # return f'{self.user.username}  {self.payment_bool }   {self.stripe_checkout_id} ' 
#         return self.stripe_checkout_id




# @receiver(post_save,sender=User)
# def create_user_payment(sender,instance,created,**kwargs):
#     if created:
#         UserPaymentModel.objects.create(user=instance)


# /////////////////////////////


from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    product_image=models.ImageField(upload_to="thumbnail")
    book_url=models.URLField()
    def __str__(self):
        return self.name

class PaymentHistory(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    payment_status=models.BooleanField()


    def __str__(self):
        return self.product.name








