from django.db import models
from django.contrib.auth.models import AbstractUser
from bms import settings
GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

CHANNEL_CHOICES = (
        ("京东商城", u"京东商城"),
        ("当当网", u"当当网")
    )
#图书分类
class Category(models.Model):
    category = models.CharField('图书分类',max_length=255,null=True,blank=True,unique=True)
    tag = models.CharField(max_length=255,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.category
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "图书分类"
        # 后台管理显示（复数）
        verbose_name_plural = "图书分类"
#中图分类法
class CLC(models.Model):
    code = models.CharField('中图分类编码',max_length=255,null=True,blank=True)
    name = models.CharField('中图分类名称',max_length=255,null=True,blank=True)
    level= models.CharField('分类层级',max_length=255,null=True,blank=True)
    parent_code=models.CharField('上级分类编码',max_length=255,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "中国图书分类法"
        # 后台管理显示（复数）
        verbose_name_plural = "中国图书分类法"
#国家
class Country(models.Model):
    country = models.CharField('国家',max_length=255,null=True,blank=True,unique=True)
    tag = models.CharField('国家简写',max_length=255,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.tag
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "国家"
        # 后台管理显示（复数）
        verbose_name_plural = "国家"
#年代
class Times(models.Model):
    times = models.CharField('时代',max_length=255,null=True,blank=True,unique=True)
    tag = models.CharField(max_length=255,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.times
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "时代"
        # 后台管理显示（复数）
        verbose_name_plural = "时代"
#朝代
class Dynasty(models.Model):
    dynasty = models.CharField('朝代',max_length=255,null=True,blank=True,unique=True)
    tag = models.CharField('简称',max_length=255,null=True,blank=True)
    order=models.IntegerField('排序',null=True,blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='创建人',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.dynasty
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "朝代"
        # 后台管理显示（复数）
        verbose_name_plural = "朝代"