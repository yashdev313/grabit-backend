# Generated by Django 4.2.3 on 2023-08-10 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0020_rename_sizemodel_sizevariantmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemsmodal',
            name='produt',
        ),
        migrations.AddField(
            model_name='cartitemsmodal',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_products', to='api.productmodel'),
        ),
        migrations.CreateModel(
            name='UserSavedModal',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_saved', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='SavedItemsModal',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saved_products', to='api.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_items', to='api.usersavedmodal')),
            ],
            bases=('api.basemodel',),
        ),
    ]
