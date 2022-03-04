# Generated by Django 3.2.7 on 2022-02-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('order_no', models.CharField(max_length=64, verbose_name='订单ID')),
                ('order_desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='订单描述')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='总定价')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='折扣价格')),
                ('order_date', models.DateField(blank=True, null=True, verbose_name='订单日期')),
                ('channel', models.CharField(max_length=64, verbose_name='订单渠道')),
                ('store', models.CharField(blank=True, max_length=100, null=True, verbose_name='商铺')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('books', models.ManyToManyField(blank=True, null=True, related_name='order2books', to='book.Book', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
    ]
