# Generated by Django 4.2.3 on 2023-09-11 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0036_alter_colorvariantmodel_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['-updated'], 'verbose_name': 'CategoryModal', 'verbose_name_plural': 'CategoryModal'},
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='colors',
            field=models.ManyToManyField(blank=True, default='', to='api.colorvariantmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(blank=True, default='', to='api.sizevariantmodel'),
        ),
        migrations.CreateModel(
            name='UserPaymentModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('payment_bool', models.BooleanField(default=False)),
                ('stripe_checkout_id', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserPaymentModel',
                'verbose_name_plural': 'UserPaymentModel',
            },
            bases=('api.basemodel',),
        ),
    ]
