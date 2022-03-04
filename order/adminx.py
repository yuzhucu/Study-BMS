import xadmin
from xadmin import views
from .models import Order
from .resources import OrderResource


# 订单自定义管理页面
class OrderAdmin(object):
    model_icon = 'fa fa-shopping-bag'

    # list_display：在后台展示的字段，可以点击列头进行排序
    list_display = ['id', 'order_no', 'books','order_desc','order_date','channel','store','order','create_time','create_user']
    # list_filter：做过滤器筛选字段，过滤框会出现在右侧
    list_filter = ['order_no', 'books','order_desc','order_date','channel','store',]
    # search_fields：可用来做搜索条件的字段（不用时间格式的字段），搜索框会出现在上侧
    search_fields = ['order_no', 'order_desc','channel','order_date','store',]
    # 设置可以在列表中直接修改的字段
    list_editable = ['order_no', 'order_desc','channel','order_date','store',]
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    # 配置插件效果
    #style_fields = {'introduce': 'ueditor','review': 'ueditor'}
    #设置后台某个字段的排序规则（加负号为倒序）
    ordering = ['-create_time','order_no']
    #在编辑页面的只读字段
    readonly_fields=[]
    #在列表页显示详情信息
    show_detail_fileds=[]
    # 导出类型 list_export设置为None来禁用数据导出功
    list_export = ('xls', 'xml', 'json','csv')
    #设置默认可编辑字段
    list_display_links=['order_no']
    # 导出字段
    list_export_fields = ['id', 'order_id', 'books','order','create_time','create_user']
    # 导入导出配置，此处也可以只配置一个导入功能或导出功能，而把另一个功能关掉
    import_export_args = {"import_resource_class": OrderResource,
                          "export_resource_class": OrderResource}


    # 自动填入当前用户
    def instance_forms(self):
        super().instance_forms()
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id


xadmin.site.register(Order,OrderAdmin)

