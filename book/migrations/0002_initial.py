# Generated by Django 3.2.7 on 2022-02-14 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, related_name='book2authors', to='book.Author', verbose_name='作者/编者'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category', verbose_name='图书分类'),
        ),
        migrations.AddField(
            model_name='book',
            name='clc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.clc', verbose_name='中图分类'),
        ),
        migrations.AddField(
            model_name='book',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.publisher', verbose_name='出版社'),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(blank=True, null=True, related_name='book2translator', to='book.Author', verbose_name='译者'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, related_name='author2books', to='book.Book', verbose_name='作品'),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(blank=True, default=1, max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.country', verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='author',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='author',
            name='dynasty',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.dynasty', verbose_name='朝代'),
        ),
        migrations.AddField(
            model_name='author',
            name='times',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.times', verbose_name='年代'),
        ),
    ]
