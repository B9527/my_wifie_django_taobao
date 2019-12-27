# Generated by Django 3.0.1 on 2019-12-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='用户名', max_length=200)),
                ('password', models.CharField(help_text='用户密码', max_length=200)),
                ('reg_time', models.DateTimeField(auto_now=True, help_text='注册时间')),
                ('user_stats', models.IntegerField(choices=[(1, '正常用户'), (0, '黑名单')], default=1, help_text='是否上架')),
                ('tel_phone', models.CharField(help_text='电话号码', max_length=200)),
                ('remark_name', models.CharField(help_text='用户备注', max_length=200)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'my_user',
                'unique_together': {('username',)},
            },
        ),
    ]