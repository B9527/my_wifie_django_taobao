# Generated by Django 3.0 on 2019-12-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_auto_20191204_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_uprice',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
