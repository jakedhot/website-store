# Generated by Django 4.1.4 on 2023-01-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_state_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Mindanao', 'Mindanao'), ('Luzon', 'Luzon'), ('Visayas', 'Visayas')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CV', 'Civet'), ('BA', 'Barako'), ('AR', 'Arabica'), ('RO', 'Robusta'), ('MO', 'Mocha')], max_length=2),
        ),
    ]
