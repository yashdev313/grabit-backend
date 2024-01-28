from django.contrib import admin

# Register your models here.
from .models import BaseModel, ProductModel, CategoryModel, SizeVariantModel, ColorVariantModel,ProductImageModal,UserCartModal,CartItemsModal,UserSavedModal,SavedItemsModal,UserAddressesModel,AddressesModel,LandingSlideModal,CategoryClassModel



class ProductImagesInline(admin.StackedInline):
    model = ProductImageModal
    fk_name = "product"

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    inlines =[ProductImagesInline]
    list_display = ['name', 'category', 'price']
    readonly_fields = ['slug']

# class CityImageInline(admin.TabularInline):
#     model = CityImage


@admin.register(LandingSlideModal)
class LandingSlideAdmin(admin.ModelAdmin):
    list_display=['name','image','image_alt','url']


# class CityAdmin(admin.ModelAdmin):
#     inlines = [CityImageInline]

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CategoryClassModel)
class CategoryClassAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SizeVariantModel)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(ColorVariantModel)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(UserSavedModal)
class UserSavedAdmin(admin.ModelAdmin):
    list_display = ['user']




@admin.register(UserCartModal)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(SavedItemsModal)
class SavedItemsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']



@admin.register(CartItemsModal)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['user','product','color_variant','size_variant']



@admin.register(UserAddressesModel)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(AddressesModel)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['full_name','mobile_number','email','city','state','pincode']



# @admin.register(FavouriteModel)
# class FavouriteAdmin(admin.ModelAdmin):
#     list_display = ['product']


# @admin.register(CartModel)
# class CartModel(admin.ModelAdmin):
#     list_display = ['product']        


@admin.register(ProductImageModal)
class ProductImageAdmin(admin.ModelAdmin):
    list_display=['product']




# fetch('http://127.0.0.1:8000/account/register', {
#         method: "POST",
#         headers: {
#             "Content-Type": "application/json"
#         },
#         body: JSON.stringify({username:'user',password:'admin'})
#     });


