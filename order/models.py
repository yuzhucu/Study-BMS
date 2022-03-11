from django.db import models
from bms import settings
from book.models import Book


class Order(models.Model):
    id=models.AutoField('序号', primary_key=True)
    order_no = models.CharField('订单ID', max_length=64)
    order_desc = models.CharField('订单描述', max_length=200,null=True,blank=True)
    books = models.ManyToManyField(to=Book,related_name='order2books',verbose_name='书籍',blank=True)
    total_price = models.DecimalField('总定价',max_digits=10, decimal_places=2,null=True,blank=True)
    discount_price = models.DecimalField('折扣价格',max_digits=10, decimal_places=2,null=True,blank=True)
    order_date=models.DateField('订单日期', null=True, blank=True)
    channel= models.CharField('订单渠道', max_length=64)
    store=models.CharField('商铺', max_length=100,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True, auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True,blank=True)

    # 字符串友好展示，在后台管理的时候生效
    def __str__(self):
        return self.order_no

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "订单"
        # 后台管理显示（复数）
        verbose_name_plural = "订单"
