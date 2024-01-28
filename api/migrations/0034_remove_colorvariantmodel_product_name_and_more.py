# Generated by Django 4.2.3 on 2023-09-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_useraddressesmodel_delievery_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorvariantmodel',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='sizevariantmodel',
            name='product_name',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='colors',
            field=models.ManyToManyField(to='api.colorvariantmodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(to='api.sizevariantmodel'),
        ),
    ]
