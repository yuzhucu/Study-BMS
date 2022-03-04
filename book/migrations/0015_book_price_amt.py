# Generated by Django 3.2.7 on 2022-02-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price_amt',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='买入数量'),
        ),
    ]
