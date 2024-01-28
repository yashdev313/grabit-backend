# Generated by Django 4.2.3 on 2024-01-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_usercartmodal_shipping_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressesmodel',
            name='alternate_mobile_number',
            field=models.CharField(blank=True, help_text='Alternate Mobile No.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='addressesmodel',
            name='mobile_number',
            field=models.CharField(help_text='Mobile No.', max_length=20),
        ),
        migrations.AlterField(
            model_name='addressesmodel',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='smDescription',
            field=models.CharField(max_length=100),
        ),
    ]