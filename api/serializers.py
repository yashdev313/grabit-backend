from rest_framework import serializers
from .models import ProductModel, CategoryModel,ProductImageModal,ColorVariantModel,SizeVariantModel,CartItemsModal,SavedItemsModal,AddressesModel,UserAddressesModel,LandingSlideModal,CategoryClassModel, UserCartModal




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =ProductImageModal
        fields = ['id','image','image_alt']







class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariantModel
        fields = ['id','name','price']


class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariantModel
        fields = ['id','name','price']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id','name','image','image_alt']


class CategoryClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryClassModel
        fields = ['id','name','image','image_alt']

class ProductSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField()'color_color','size__size'
    # category_name = serializers.SerializerMethodField(source='color_color')
    # category_name = serializers.SerializerMethodField()#'color_color','size__size'
    product_images = ProductImageSerializer(many=True)
    # cs = serializers.CharField(source='color')
    colors = ColorVariantSerializer(many=True)
    sizes = SizeVariantSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = ProductModel
        fields = ['id','name','thumbnail','thumbnail_alt','product_images','smDescription','description','colors','sizes','category','price','slug']
        # fields = ['id','name','thumbnail','product_images','color_variants','size_variants']


class LandingSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model=LandingSlideModal
        fields=['id','image','image_alt','url']



#     def get_category_name(self,obj):
#         # print(obj.color_variant,'scs')
#         return obj.category.name.lower()
# # # ProductImageModal
#     def get_prods(self,obj):
#         return obj.product_image_modal_set.all()






class SavedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model =SavedItemsModal
        fields ='__all__'

class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCartModal
        fields = ('id','number_of_items','total_price','get_shipping_charge','cart_total_price',)

class CartItemsSerializer(serializers.ModelSerializer):
    # cart_products =ProductSerializer()
    # color_variant = ColorVariantModel()
    class Meta:
        model=CartItemsModal
        # fields = '__all__'
        fields = ['id','name','thumbnail','thumbnail_alt','color','size','quantity','price','item_total_price','number_of_items','slug']

# class CartItemRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
#     class Meta:
#         model =CartItemsModal
#         fields = ('quantity',)

#     def update


        # def validate(self,data):
        #     pincode = data.get('pincode')
        #     if(type(pincode) != number ):
        #         raise serializers.ValidationError("Pincode should be a number.")



class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddressesModel
        # fields = '__all__'
        exclude=('user',)


class UserAddressesSerializer(serializers.ModelSerializer):
    # addresses =AddressesSerializer(source='addresses.user.user')
    class Meta:
        model=UserAddressesModel
        # fields=['addresses']
        fields =['delievery_address', 'first_name', 'last_name', 'mobile_number', 'alternate_mobile_number', 'email', 'street', 'landmark', 'city', 'state', 'country', 'pincode']

    



# class SavedSerializer(serializers.ModelSerializer):
#     product_name = serializers.SerializerMethodField()
#     # product_img = serializers.SerializerMethodField()
#     product_price = serializers.SerializerMethodField()
#     product_slug= serializers.SerializerMethodField()

    
#     class Meta:
#         model = FavouriteModel
#         # fields = '__all__'
#         fields = ['product_name','product_price','product_slug']

#     def get_product_name(self,obj):
#         return obj.product.slug

#     # def get_product_img(self,obj):
#     #     return obj.product.img

#     def get_product_slug(self,obj):
#         return obj.product.slug

#     def get_product_price(self,obj):
#         return obj.product.price


# class CartSerializer(serializers.ModelSerializer):
#     product_name = serializers.SerializerMethodField()
#     # product_img = serializers.SerializerMethodField()
#     product_price = serializers.SerializerMethodField()
#     product_slug= serializers.SerializerMethodField()


#     class Meta:
#         model = CartModel
#         fields = ['product_name','product_price','product_slug']




#     def get_product_name(self,obj):
#         return obj.product.slug

#     # def get_product_img(self,obj):
#     #     return obj.product.img

#     def get_product_slug(self,obj):
#         return obj.product.slug

#     def get_product_price(self,obj):
#         return obj.product.price
