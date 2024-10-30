# Generated by Django 5.0.7 on 2024-10-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_customer_state_alter_product_category_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='razorpay_order_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='razorpay_payment_status',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('COD', 'Cash on Delivery'), ('Online', 'Online Payment')], default='COD', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Mindanao', 'Mindanao'), ('Luzon', 'Luzon'), ('Visayas', 'Visayas')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On The Way', 'On The Way'), ('Cancel', 'Cancel'), ('Packed', 'Packed'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BA', 'Barako'), ('RO', 'Robusta'), ('AR', 'Arabica'), ('MO', 'Mocha'), ('CV', 'Civet')], max_length=2),
        ),
    ]