# Generated by Django 3.2.7 on 2022-02-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20220214_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name_pinyin',
            field=models.SlugField(blank=True, max_length=64, null=True, unique=True, verbose_name='名称拼音'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='name_pinyin',
            field=models.SlugField(blank=True, max_length=64, null=True, unique=True, verbose_name='名称拼音'),
        ),
    ]
