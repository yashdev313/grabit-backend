# Generated by Django 4.2.3 on 2023-12-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_remove_usercartmodal_shipping_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercartmodal',
            name='shipping_charge',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
