# Generated by Django 3.2.7 on 2022-02-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='图书分类')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '图书分类',
                'verbose_name_plural': '图书分类',
            },
        ),
        migrations.CreateModel(
            name='CLC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='中图分类编码')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='中图分类名称')),
                ('level', models.CharField(blank=True, max_length=255, null=True, verbose_name='分类层级')),
                ('parent_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='上级分类编码')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '中国图书分类法',
                'verbose_name_plural': '中国图书分类法',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='国家')),
                ('tag', models.CharField(blank=True, max_length=255, null=True, verbose_name='国家简写')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '国家',
                'verbose_name_plural': '国家',
            },
        ),
        migrations.CreateModel(
            name='Dynasty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dynasty', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='朝代')),
                ('tag', models.CharField(blank=True, max_length=255, null=True, verbose_name='简称')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '朝代',
                'verbose_name_plural': '朝代',
            },
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='时代')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '时代',
                'verbose_name_plural': '时代',
            },
        ),
    ]
