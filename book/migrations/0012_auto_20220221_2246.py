# Generated by Django 3.2.7 on 2022-02-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, related_name='book2authors', to='book.Author', verbose_name='作者/编者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(blank=True, null=True, related_name='book2translator', to='book.Author', verbose_name='译者'),
        ),
    ]
