from import_export import resources
from .models import Book,Publisher,Author

#使用  django-import-export 导入导出，如不使用可不用该类
class BookResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Book
        # 定义导出数据的字段
        fields = ['id', 'title', 'authors', 'publisher', 'price','publishDate', 'category', 'pages', 'order']
        # 定义不导出的字段
        # exclude = []

class AuthorResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Author
        # 定义导出数据的字段
        fields = ['id', 'name', 'country','dynasty','times','name_en','gender','introduce','order','create_user','create_time']

        # 定义不导出的字段
        # exclude = []

class PublisherResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Publisher
        # 定义导出数据的字段
        fields = ['id', 'name', 'addr','order','create_time','create_user']

        # 定义不导出的字段
        # exclude = []

