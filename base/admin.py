from .models import Country,Category,Times,Dynasty,CLC
from user.models import UserProfile
from .resources import CLCResource,DynastyResource,CategoryResource,CountryResource,TimesResource
from django.contrib import admin

# 国家码表
class CountryAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'country','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'country']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'country']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['id']
    list_editable = ['country','tag','order','create_user']
    import_export_args = {"import_resource_class": CountryResource,
                          "export_resource_class": CountryResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
admin.site.register(Country,CountryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'category','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'category']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'category']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['id']
    list_editable = ['category','tag','order','create_user']
    import_export_args = {"import_resource_class": CategoryResource,
                          "export_resource_class": CategoryResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
admin.site.register(Category,CategoryAdmin)

class CLCAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'code','name','level','parent_code','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'code','name','level','parent_code']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'code','name','level','parent_code']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['id']
    list_editable = ['code','name','level','parent_code','create_user']

    exclude = ('id',)
    list_import_fields=[ 'code','name','level','parent_code','order']
    import_export_args = {"import_resource_class": CLCResource,
                          "export_resource_class": CLCResource}

    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
admin.site.register(CLC,CLCAdmin)

class TimesAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'times','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'times']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'times']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['id']
    list_editable = ['times','tag','order','create_user']
    import_export_args = {"import_resource_class": TimesResource,
                          "export_resource_class": TimesResource}

    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
admin.site.register(Times,TimesAdmin)

class DynastyAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'dynasty','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'dynasty']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'dynasty']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['id']
    list_editable = [ 'dynasty','tag','order','create_user']

    #导出字段
    list_export_fields =['id','dynasty','tag','order','create_time','create_user']
    import_export_args = {"import_resource_class": DynastyResource,
                          "export_resource_class": DynastyResource}

    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
admin.site.register(Dynasty,DynastyAdmin)
