# Generated by Django 4.2.3 on 2023-07-20 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizemodel',
            name='product_name',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='size', to='api.productmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='varientmodel',
            name='product_name',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='varients', to='api.productmodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sizemodel',
            name='size',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='varientmodel',
            name='varients',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
