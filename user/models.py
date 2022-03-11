from django.db import models
from django.contrib.auth.models import AbstractUser
from bms import settings
# 用户的类
#class UserProfile(models.Model):
class UserProfile(AbstractUser):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('用户名', max_length=32,unique=True)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱',null=True,blank=True)
    mobile = models.IntegerField('手机',null=True,blank=True)
    orderno = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    create_user = models.ForeignKey('UserProfile', verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True,related_name='cup')
    def __str__(self):
        return self.username
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "用户信息"
        # 后台管理显示（复数）
        verbose_name_plural = "用户信息"

GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )