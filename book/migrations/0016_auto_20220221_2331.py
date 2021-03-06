# Generated by Django 3.2.7 on 2022-02-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_book_price_amt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price_amt',
            new_name='buy_amt',
        ),
        migrations.AddField(
            model_name='book',
            name='buy_date',
            field=models.DateField(blank=True, null=True, verbose_name='买入日期'),
        ),
    ]
