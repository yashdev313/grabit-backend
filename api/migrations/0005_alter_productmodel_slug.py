# Generated by Django 4.2.3 on 2023-07-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_title_productmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]