from django.db import models


# Create your models here.

class UserModel(models.Model):
    """
    用户
    """
    stats_choices = [
        (1, "正常用户"),
        (0, "黑名单")
    ]

    user_name = models.CharField(max_length=200, help_text="用户名")
    password = models.CharField(max_length=200, help_text="用户密码")
    reg_time = models.DateTimeField(auto_now=True, help_text="注册时间")
    user_stats = models.IntegerField(help_text='是否上架', choices=stats_choices, default=1)
    tel_phone = models.CharField(max_length=200, help_text="电话号码", null=True, blank=True)
    remark_name = models.CharField(max_length=200, help_text="用户备注", null=True, blank=True)

    def __str__(self):
        return self.user_name + "__" + self.remark_name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        db_table = "my_user"
        unique_together = ["user_name"]
