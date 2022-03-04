from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = '图书管理'
    name = 'book'
    orderIndex=1
