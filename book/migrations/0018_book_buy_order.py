# Generated by Django 3.2.7 on 2022-02-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_alter_book_translator'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='buy_order',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='订单号'),
        ),
    ]
