# Generated by Django 3.0.1 on 2019-12-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20191226_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='username',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='remark_name',
            field=models.CharField(blank=True, help_text='用户备注', max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='usermodel',
            unique_together={('user_name',)},
        ),
    ]
