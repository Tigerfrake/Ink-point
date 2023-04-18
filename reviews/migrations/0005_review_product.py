# Generated by Django 4.1.6 on 2023-02-20 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_cart_consent_alter_order_means_of_payment_and_more'),
        ('reviews', '0004_delete_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]
