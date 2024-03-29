# Generated by Django 4.2.3 on 2023-09-01 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_cartitemsmodal_item_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressesmodel',
            name='delievery_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='default_address', to='api.addressesmodel'),
        ),
        migrations.AlterField(
            model_name='usercartmodal',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
