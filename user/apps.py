from django.apps import AppConfig

class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = '用户管理'
    orderIndex=3
