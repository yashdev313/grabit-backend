# Generated by Django 4.2.3 on 2023-08-10 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0015_ladingslidemodal_image_alt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemsModal',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
            ],
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='UserCartModal',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cart', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.basemodel',),
        ),
        migrations.AlterModelOptions(
            name='productimagemodal',
            options={'verbose_name_plural': 'ProductImageModal'},
        ),
        migrations.RenameModel(
            old_name='VarientModel',
            new_name='ColorVarientModel',
        ),
        migrations.DeleteModel(
            name='CartModel',
        ),
        migrations.AddField(
            model_name='cartitemsmodal',
            name='color_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color_variant', to='api.colorvarientmodel'),
        ),
        migrations.AddField(
            model_name='cartitemsmodal',
            name='produt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='api.productmodel'),
        ),
        migrations.AddField(
            model_name='cartitemsmodal',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size_variant', to='api.sizemodel'),
        ),
        migrations.AddField(
            model_name='cartitemsmodal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='api.usercartmodal'),
        ),
    ]
