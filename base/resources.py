from import_export import resources
from .models import Country,Category,Times,Dynasty,CLC

#使用  django-import-export 导入导出，如不使用可不用该类

class CLCResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = CLC
        # 定义导出数据的字段
        fields = ['id','code','name','level','parent_code','order','create_time','create_user']
        # 定义不导出的字段
        # exclude = []

class CountryResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Country
        # 定义导出数据的字段
        fields = ['id','country','tag','order','create_time','create_user']
        # 定义不导出的字段
        # exclude = []

class CategoryResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Category
        # 定义导出数据的字段
        fields = ['id','category','tag','order','create_time','create_user']
        # 定义不导出的字段
        # exclude = []

class TimesResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Times
        # 定义导出数据的字段
        fields = ['id','times','tag','order','create_time','create_user']
        # 定义不导出的字段
        # exclude = []

class DynastyResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Dynasty
        # 定义导出数据的字段
        fields =['id','dynasty','tag','order','create_time','create_user']
        # 定义不导出的字段
        # exclude = []

