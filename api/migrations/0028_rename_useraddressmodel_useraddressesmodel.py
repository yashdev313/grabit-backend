# Generated by Django 4.2.3 on 2023-08-11 05:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0027_alter_addressesmodel_pincode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddressModel',
            new_name='UserAddressesModel',
        ),
    ]
