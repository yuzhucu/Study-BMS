from import_export import resources
from .models import Order

class OrderResource(resources.ModelResource):
    """自定义导入导出功能类"""
    class Meta:
        model = Order
        # 定义导出数据的字段
        fields = ['id', 'order_id', 'books',  'order']
        # 定义不导出的字段
        # exclude = []
