# Generated by Django 4.2.3 on 2023-08-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_productmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
