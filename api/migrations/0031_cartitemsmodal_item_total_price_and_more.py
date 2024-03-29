# Generated by Django 4.2.3 on 2023-08-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_cartitemsmodal_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemsmodal',
            name='item_total_price',
            field=models.DecimalField(decimal_places=2, default=32, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercartmodal',
            name='number_of_items',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usercartmodal',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cartitemsmodal',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
