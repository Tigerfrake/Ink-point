# Generated by Django 4.1.5 on 2023-02-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_review_alter_cart_consent_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AlterField(
            model_name='order',
            name='means_of_payment',
            field=models.CharField(choices=[('mpesa', 'M-pesa'), ('bank', 'Bank'), ('cash', 'Cash')], default='cash', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('cart', 'Cart'), ('completed', 'Completed')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('out_of_stock', 'Out of Stock'), ('available', 'Available')], default='available', max_length=50),
        ),
    ]