from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = '基础数据管理'
    name = 'base'
    orderIndex=4
