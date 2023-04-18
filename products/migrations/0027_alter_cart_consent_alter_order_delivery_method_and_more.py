# Generated by Django 4.1.6 on 2023-02-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_cart_consent_alter_order_means_of_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='consent',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('door-delivery', 'Door delivery'), ('dispatch-store', 'Dispatch store')], default='door-delivery', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('mpesa', 'M-pesa'), ('cash', 'Cash'), ('bank', 'Bank')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('cart', 'Cart'), ('pending', 'Pending')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]