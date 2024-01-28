import uuid
from django.db import models
# from django.utils.text import slugify
from django.template.defaultfilters import slugify

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# main logic starts from Here

STATUS_CHOICES = (
   ('Draft','Draft'),
   ('Publish','Publish'),
)


class ProductModel(BaseModel):
    name = models.CharField(
        max_length=300, editable=True, blank=False, null=False)
    img = models.ImageField()
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(
        'CategoryModel', null=True, on_delete=models.SET_NULL, related_name='category')
    slug = models.SlugField(unique=True, blank=True, null=False)
    status = models.CharField(max_length=7,choices=STATUS_CHOICES,default='Draft')
    


    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.name} {self.slug}"



    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name





class CategoryModel(BaseModel):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(CategoryModel, self).save(*args, **kwargs)


class FavouriteModel(BaseModel):
    product = models.OneToOneField('ProductModel', on_delete=models.CASCADE)

    # @property
    # def full_name(self):
    #     "Returns the person's full name."
    #     return f"{self.product}"


class CartModel(BaseModel):
    product = models.OneToOneField('ProductModel', on_delete=models.CASCADE)


class SizeModel(BaseModel):
    product_name = models.ForeignKey(
        'ProductModel', on_delete=models.CASCADE, related_name='size')
    size = models.CharField(max_length=5, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.product_name}'


class VarientModel(BaseModel):
    product_name = models.ForeignKey(
        'ProductModel', on_delete=models.CASCADE, related_name='varients')
    varients = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.product_name}   {self.varients}'


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
