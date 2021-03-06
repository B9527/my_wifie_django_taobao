# Generated by Django 3.0 on 2019-12-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_pid', models.IntegerField()),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
                'unique_together': {('category_name',)},
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('product_uprice', models.DecimalField(decimal_places=2, max_digits=2)),
                ('product_num', models.IntegerField()),
                ('product_detail', models.TextField()),
                ('product_img_url', models.CharField(max_length=500)),
                ('is_store', models.IntegerField(choices=[(1, '现货'), (0, '非现货')], default=2, verbose_name='是否现货')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products_app.Category')),
            ],
            options={
                'db_table': 'product',
                'unique_together': {('product_name',)},
            },
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.Products')),
            ],
            options={
                'db_table': 'product_image',
            },
        ),
    ]
