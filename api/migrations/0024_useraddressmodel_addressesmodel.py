# Generated by Django 4.2.3 on 2023-08-11 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0023_rename_ladingslidemodal_landingslidemodal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddressModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserAddressModal',
                'verbose_name_plural': 'UserAddressModal',
            },
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='AddressesModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('first_name', models.CharField(help_text='Enter Your First Name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter Your Last Name', max_length=20)),
                ('mobile_number', models.IntegerField(help_text='Mobile No.')),
                ('alternate_mobile_number', models.IntegerField(blank=True, help_text='Alternate Mobile No.', null=True)),
                ('email', models.EmailField(help_text='Email Address', max_length=254)),
                ('street', models.CharField(help_text='Street Address', max_length=100)),
                ('landmark', models.CharField(help_text='Landmark', max_length=100)),
                ('city', models.CharField(help_text='Enter Your city', max_length=20)),
                ('state', models.CharField(help_text='Enter Your state', max_length=20)),
                ('country', models.CharField(default='India', help_text='Enter Your country', max_length=20)),
                ('pincode', models.IntegerField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AddressesModel',
                'verbose_name_plural': 'AddressesModel',
            },
            bases=('api.basemodel',),
        ),
    ]