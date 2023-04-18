# Generated by Django 4.1.6 on 2023-02-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_cart_consent_alter_order_means_of_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('bank', 'Bank'), ('cash', 'Cash'), ('mpesa', 'M-pesa')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cart', 'Cart')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]