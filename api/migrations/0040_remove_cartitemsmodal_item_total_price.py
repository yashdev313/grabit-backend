# Generated by Django 4.2.3 on 2023-09-19 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_categorymodel_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitemsmodal',
            name='item_total_price',
        ),
    ]
