import uuid
from django.db import models
# from django.utils.text import slugify
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField 
# Create your models here.
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# 

from django.dispatch import receiver
from django.db.models.signals import post_save

# 




class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)






# main logic starts from Here

STATUS_CHOICES = (
   ('Draft','Draft'),
   ('Publish','Publish'),
)




class LandingSlideModal(BaseModel):
    name =  models.CharField(max_length=100,blank=True,null=False)
    image = models.ImageField()
    image_alt = models.CharField(max_length=100,blank=False,null=False)
    url = models.CharField(max_length=50,blank=True,null=False)


    class Meta:
        verbose_name= "LandingSlideModal"
        verbose_name_plural = "LandingSlideModal"


    def __str__(self):
        return self.name



class ProductModel(BaseModel):
    name = models.CharField(
        max_length=300, editable=True, blank=False, null=False)
    thumbnail = models.ImageField()
    thumbnail_alt = models.CharField(max_length=50,blank=False,null=False)
    smDescription = models.CharField(max_length=100,blank=False,null=False)

    description = RichTextUploadingField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(
        'CategoryModel',null=True, on_delete=models.SET_NULL, related_name='category')
    category_class = models.ForeignKey(
        'CategoryClassModel',null=True, on_delete=models.SET_NULL, related_name='category_class')
    slug = models.SlugField(unique=True, blank=True, null=False)
    status = models.CharField(max_length=7,choices=STATUS_CHOICES,default='Draft')
    colors = models.ManyToManyField('ColorVariantModel',blank=True,default='' )
    sizes = models.ManyToManyField('SizeVariantModel',blank=True ,default='')



    class Meta:
        verbose_name= "ProductModel"
        verbose_name_plural = "ProductModel"


    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.name} {self.slug}"


    # @property
    # def image_list(self):
    #     # return self.event_set
    #     return self.product_image_modal_set


    @property
    def category_name(self):
        return self.category.name


    def save(self, *args, **kwargs):
        # if self.id and self.colors:
        #     print(self.colors)
                # if not self.colors:
        #     self.colors.clear()

        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImageModal(BaseModel):
    product = models.ForeignKey(
        'ProductModel', null=True, on_delete=models.SET_NULL, related_name='product_images')
    image = models.ImageField()
    image_alt = models.CharField(max_length=50,blank=False,null=False)
    # image = models.ImageField()

    class Meta:
        verbose_name= "ProductImageModal"
        verbose_name_plural = "ProductImageModal"

    # def __str__(self):
    #     return self.image_alt







class CategoryModel(BaseModel):
    name = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField()
    image_alt = models.CharField(max_length=50,blank=False,null=False)
    


    class Meta:
        verbose_name= "CategoryModal"
        verbose_name_plural = "CategoryModal"
        ordering = ['-updated']

    # def repr(self):
    #     return self.name
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(CategoryModel, self).save(*args, **kwargs)


# class FavouriteModel(BaseModel):
#     product = models.OneToOneField('ProductModel', on_delete=models.CASCADE)

#     # @property
#     # def full_name(self):
#     #     "Returns the person's full name."
#     #     return f"{self.product}"

#     # @property
#     # def pr(self):
#     #     return self.product.img



class CategoryClassModel(BaseModel):
    name = models.CharField(max_length=20, blank=False, null=False)
    image = models.ImageField()
    image_alt = models.CharField(max_length=50,blank=False,null=False)



    class Meta:
        verbose_name= "CategoryClassModel"
        verbose_name_plural = "CategoryClassModel"
        # ordering = ['created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(CategoryClassModel, self).save(*args, **kwargs)



class UserSavedModal(BaseModel):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_saved')

    # is_paid = models.BooleanField(default=False)


    class Meta:
        verbose_name= "UserSavedModal"
        verbose_name_plural = "UserSavedModal"


    def __str__(self):
        return self.user.email

class SavedItemsModal(BaseModel):
    user =  models.ForeignKey(UserSavedModal,on_delete=models.CASCADE,related_name='saved_items')
    product = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,blank=True,null=True,related_name='saved_products')
    # color_variant = models.ForeignKey('ColorVariantModel',on_delete=models.SET_NULL,blank=True,null=True,related_name='color_variant')
    # size_variant = models.ForeignKey('SizeModel',on_delete=models.SET_NULL,blank=True,null=True,related_name='size_variant')

    class Meta:
        verbose_name= "SavedItemsModal"
        verbose_name_plural = "SavedItemsModal"


class UserCartModal(BaseModel):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_cart')
    # number_of_items = models.PositiveIntegerField(
    #     default=0, null=True, blank=True)
    # total_price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2,blank=True)
    shipping_charge = models.IntegerField(default=0, blank=True)
    is_paid = models.BooleanField(default=False)


    class Meta:
        verbose_name= "UserCartModal"
        verbose_name_plural = "UserCartModal"

    def total_price(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price*cart_item.quantity)
            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant_price)
            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)
        return sum(price)

    @property
    def cart_total_price(self):
        total_price = self.total_price()
        if total_price < self.shipping_charge:
            return total_price + self.shipping_charge
        return total_price

    @property
    def number_of_items(self):
        return self.cart_items.count()

    @property
    def get_shipping_charge(self):
        total_price = self.total_price()
        if total_price < self.shipping_charge:
            return self.shipping_charge
        return 0

    def save(self, *args, **kwargs):
        # self.item_total_price = self.product.price*quantity
        # print('hii',CartItemsModal.objects.count()
        # sum([item['item_total_price'] for item in self.cart_items])
# )
        # self.number_of_items = self.cart_items.count()

        # # print(self.cart_items.count())
        # # print(self.cart_items.all()[1].price)

        # # print(sum([item['item_total_price'] for item in self.cart_items])
# )
        # self.number_of_items = CartItemsModal.objects.count()
        super(UserCartModal, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.email



class CartItemsModal(BaseModel):
    user =  models.ForeignKey(UserCartModal,on_delete=models.CASCADE,related_name='cart_items')
    product = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,blank=True,null=True,related_name='cart_products')
    color_variant = models.ForeignKey('ColorVariantModel',on_delete=models.SET_NULL,blank=True,null=True,related_name='color_variant')
    size_variant = models.ForeignKey('SizeVariantModel',on_delete=models.SET_NULL,blank=True,null=True,related_name='size_variant')
    quantity = models.PositiveIntegerField(blank=False,null=False,default=1)
    item_total_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)


    class Meta:
        verbose_name= "CartItemsModal"
        verbose_name_plural = "CartItemsModal"

    @property
    def name(self):
        return self.product.name

    @property
    def thumbnail(self):
        return self.product.thumbnail.url

    @property
    def thumbnail_alt(self):
        return self.product.thumbnail_alt


    @property
    def price(self):
        return self.product.price


    @property
    def color(self):
        return self.color_variant.name

    @property
    def size(self):
        return self.size_variant.name


    def save(self, *args, **kwargs):
        # self.item_total_price = self.product.price*self.quantity
        super(CartItemsModal, self).save(*args, **kwargs)


    @property
    def number_of_items(self):
        return self.user.number_of_items


    @property
    def total_price(self):
        return self.user.cart_total_price

    def __str__(self):
       return self.product.name

    @property
    def slug(self):
        return self.product.slug

    @property    
    def item_total_price(self):
        price = [self.product.price*self.quantity]

        if self.color_variant:
            color_variant_price = self.color_variant.price
            price.append(color_variant_price)
        if self.size_variant:
            size_variant_price = self.size_variant.price
            price.append(size_variant_price)

        return sum(price)

    @property
    def number_of_items(self):
        # user_cart = UserCartModal.objects.filter(user =self.user.user,is_paid=False).cart_items.all()
        user_cart = UserCartModal.objects.filter(user=self.user.user,is_paid=False).first()
        user_cart = CartItemsModal.objects.filter(user=user_cart)
        return len(user_cart)
    def total_price(self):

        user_cart = UserCartModal.objects.filter(user=self.user.user,is_paid=False).first()
        # user_cart = CartItemsModal.objects.filter(user=user_cart)
        cart_items = CartItemsModal.objects.filter(user=user_cart)
        price = []

        for cart_item in cart_items:
            price.append(cart_item.product.price*cart_item.quantity)
            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant_price)
            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)
        return sum(price)

    class Meta:
        verbose_name_plural="CartItemsModal"



 

class SizeVariantModel(BaseModel):
    # product_name = models.ForeignKey(
    #     'ProductModel', on_delete=models.CASCADE, related_name='size_variants')
    name = models.CharField(max_length=5, blank=True, null=True)
    price = models.IntegerField(blank=True,null=True,default=0)


    class Meta:
        verbose_name= "SizeVariantModel"
        verbose_name_plural = "SizeVariantModel"


    def __str__(self):
        return f'{self.name}'



class ColorVariantModel(BaseModel):
    # product_name = models.ForeignKey(
    #     'ProductModel', on_delete=models.CASCADE, related_name='color_variants')
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True,default=0)


    class Meta:
        verbose_name= "ColorVariantModel"
        verbose_name_plural = "ColorVariantModel"



    def __str__(self):
        return f'{self.name}'


# class Post(models.Model):
#     content = models.TextField()

# class Comment(models.Model):
#     comment_content = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_rel')
#     created_at = models.DateTimeField(auto_add_now=True)


# # get all comments for a given post created in last 1 week
# last_one_week_dt = timezone.now() - timezone.deltatime(days=7)
# comments = Post.objects.filter(
#     id= 10,
#     comments_rel__created_at__gte=last_one_week_dt
# )

# # or use the below syntax
# comments = Post.objects.get(id=10).comments_rel.filter(
#   created_at__gte=last_one_week_dt
# )



# First Name - Last Name
# Mobile.No
# Alternate Mobile No.
# Email Address
# Street Address
# LandMark
# City 
# State
# Country
# Pincode



class UserAddressesModel(BaseModel):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_address')
    delievery_address = models.OneToOneField('AddressesModel',on_delete=models.SET_NULL,blank=True,null=True,related_name='default_address')


    class Meta:
        verbose_name= "UserAddressModal"
        verbose_name_plural = "UserAddressModal"


    # this property is named "ids" because if we name it "id" it collides with default "id" of "UserAddressesModel" and gives unexpected errors
    # @property
    # def ids(self):
    #     return self.delievery_address.id


    # def save(self, *args, **kwargs):
    #     self.user =self.user.user
    #     super(UserAddressesModel, self).save(*args, **kwargs)

    @property
    def first_name(self):
        return self.delievery_address.first_name

    @property
    def last_name(self):
        return self.delievery_address.last_name

    @property
    def full_name(self):
        return f'{self.delievery_address.first_name} {self.delievery_address.last_name}'

    @property
    def mobile_number(self):
        return self.delievery_address.mobile_number

    @property
    def alternate_mobile_number(self):
        return self.delievery_address.alternate_mobile_number

    @property
    def email(self):
        return self.delievery_address.email

    @property
    def street(self):
        return self.delievery_address.street

    @property
    def landmark(self):
        return self.delievery_address.landmark

    @property
    def city(self):
        return self.delievery_address.city

    @property
    def state(self):
        return self.delievery_address.state

    @property
    def country(self):
        return self.delievery_address.country

    @property
    def pincode(self):
        return self.delievery_address.pincode


    def __str__(self):
        return self.user.email


class AddressesModel(BaseModel):
    user =  models.ForeignKey(UserAddressesModel,on_delete=models.CASCADE,related_name='addresses')
    first_name = models.CharField(max_length=20,blank=False,null=False,help_text='Enter Your First Name')
    last_name = models.CharField(max_length=20,blank=False,null=False,help_text='Enter Your Last Name')
    mobile_number = models.CharField(max_length=20, blank=False,null=False,help_text="Mobile No.")   
    alternate_mobile_number = models.CharField(max_length=20, blank=True,null=True,help_text="Alternate Mobile No.")
    email = models.EmailField(blank=False,null=False,help_text="Email Address") 
    street = models.CharField(max_length=100,blank=False,null=False,help_text='Street Address')
    landmark = models.CharField(max_length=100,blank=False,null=False,help_text='Landmark')
    city = models.CharField(max_length=20,blank=False,null=False,help_text='Enter Your city')
    state = models.CharField(max_length=20,blank=False,null=False,help_text='Enter Your state')
    country = models.CharField(max_length=20,blank=True,null=False,default="India" , help_text='Enter Your country')
    pincode = models.CharField(max_length=6, blank=False,null=False)



    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # @property
    # def delievery_address(self):
    #     return self.user.delievery_address


    class Meta:
        verbose_name= "AddressesModel"
        verbose_name_plural = "AddressesModel"




# @receiver(post_save,sender=CartItemsModal)
# def update_user_cart_model(sender,instance,created,**kwargs):
#     if created:
#         rr = UserCartModal.objects.get(user=instance)
#         # rr.total_price = 
#         # UserCartModal.objects.update(user=request.user,total_price=instanc)

#         # UserPaymentModel.objects.create(user=instance)