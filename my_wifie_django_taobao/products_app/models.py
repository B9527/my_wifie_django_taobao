from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    """
    分类
    """
    category_id = models.AutoField(primary_key=True)  # 分类id
    category_pid = models.IntegerField()  # 分类pid
    category_name = models.CharField(max_length=200)  # 分类名

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"
        unique_together = ["category_name"]


class Products(models.Model):
    """
    商品
    """
    store_status = (
        (1, "现货"),
        (0, "非现货")
    )

    is_on_status = (
        (1, "上架"),
        (0, "下架")
    )

    product_id = models.AutoField(primary_key=True)  # 商品id
    product_name = models.CharField(max_length=200)  # 商品名
    product_price = models.DecimalField(max_digits=7, decimal_places=2)  # 商品价格
    product_uprice = models.DecimalField(max_digits=7, decimal_places=2, null=True)  # 商品原来价格
    product_num = models.IntegerField()  # 商品数量
    product_detail = models.TextField()  # 商品描述
    product_img_url = models.CharField(max_length=500)  # 商品主图
    category_id = models.ForeignKey("Category", models.SET_NULL, null=True)  # 分类id
    is_store = models.IntegerField('是否现货', choices=store_status, default=0)
    is_on = models.IntegerField('是否上架', choices=store_status, default=1)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "product"
        unique_together = ["product_name"]


class ProductsImage(models.Model):
    """
    图片
    """
    image_id = models.AutoField(primary_key=True)  # 图片id
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return self.image_url

    class Meta:
        db_table = "product_image"
