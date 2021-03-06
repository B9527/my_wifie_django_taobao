# Generated by Django 3.0 on 2019-12-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0004_auto_20191204_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(help_text='分类名，例如：手机，零食，化妆品。。。', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_pid',
            field=models.IntegerField(help_text='分类id,请填写5位数字，从10000开始', unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_detail',
            field=models.TextField(help_text='商品描述'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_img_url',
            field=models.CharField(help_text='商品主图', max_length=500),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(help_text='商品名', max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_num',
            field=models.IntegerField(help_text='商品数量'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.DecimalField(decimal_places=2, help_text='商品现价格', max_digits=7),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_uprice',
            field=models.DecimalField(decimal_places=2, help_text='商品原来价格', max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='productsimage',
            name='image_url',
            field=models.CharField(help_text='商品图片，一个商品展示多个图片，在这里一个个添加', max_length=500),
        ),
    ]
