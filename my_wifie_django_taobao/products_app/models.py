from django.db import models


class Category(models.Model):
    """
    分类
    """
    category_id = models.AutoField(primary_key=True)  # 分类idl
    category_pid = models.IntegerField(unique=True, help_text="分类id,请填写5位数字，从10000开始")  # 分类pid
    category_name = models.CharField(max_length=200, help_text="分类名，例如：手机，零食，化妆品。。。")  # 分类名

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = '商品分类'
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
    product_name = models.CharField(max_length=200, help_text="商品名")
    product_price = models.DecimalField(max_digits=7, decimal_places=2, help_text="商品现价格")
    product_uprice = models.DecimalField(max_digits=7, decimal_places=2, null=True, help_text="商品原来价格")
    product_num = models.IntegerField(help_text="商品数量")  # 商品数量
    product_detail = models.TextField(help_text="商品描述")  # 商品描述
    product_img_url = models.ImageField(upload_to='shop_image', verbose_name='商品主图', null=True)  # 商品主图
    category_id = models.ForeignKey("Category", models.SET_NULL, null=True)  # 分类id
    is_store = models.IntegerField('是否现货', choices=store_status, default=0)
    is_on = models.IntegerField('是否上架', choices=is_on_status, default=1)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
        db_table = "product"
        unique_together = ["product_name"]


class ProductsImage(models.Model):
    """
    图片
    """
    image_id = models.AutoField(primary_key=True)  # 图片id
    product = models.ForeignKey("Products", on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='shop_image', verbose_name='图片', null=True)

    def __str__(self):
        return self.product.product_name + "/"+self.image_url.name.split('/')[1]

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'
        db_table = "product_image"


class OrderModel(models.Model):
    pass

