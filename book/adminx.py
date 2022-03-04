from .models import Book,Publisher,Author
from .resources import BookResource,PublisherResource,AuthorResource
import xadmin
from xadmin.layout import Fieldset,Main,Side,Row
# 书籍自定义管理页面
class BookAdmin(object):
    model_icon = 'fa fa-book'
    def instance_forms(self):
        super().instance_forms()
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'publisher':
            kwargs['queryset'] = Publisher.objects.order_by('name_pinyin')
        if db_field.name == 'authors':
            kwargs['queryset']=Author.objects.order_by('name_pinyin')
        return super(BookAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def upload_img(self, obj):
        try:
            img = mark_safe(
                '<a href="%s" target="_blank"><img src="%s" width="90px"></a> ' % (obj.image.url, obj.image.url))
        except Exception as e:
                print(e)
                img = ''
        return img
    def get_form_layout(self):
        self.form_layout=(
            Main(
                Fieldset('图书基本信息','name','title','title_en','authors','publisher','publishDate','URL','imgsrc','ISBN')
            ),
            Side(
                Fieldset('图书购买信息','price','buy_price','buy_date','buy_order','channel','category','product_id','buy_amt')
            )
        )
        return super(BookAdmin, self).get_form_layout()

    upload_img.short_description = '图书封面'
    autocomplete_fields=['authors',]
    raw_id_fields=['publisher',]
    # list_display：在后台展示的字段，可以点击列头进行排序
    list_display = ['id', 'name','title', 'authors','publisher','publishDate','image_img2','price','buy_price','buy_order','buy_amt','buy_date','ISBN','category','pages','upload_img','channel','lables','order','create_user','create_time','update_time']
    # list_filter：做过滤器筛选字段，过滤框会出现在右侧
    list_filter = ['title', 'authors','publisher','publishDate','pages','category','lables','buy_order','buy_date']
    # search_fields：可用来做搜索条件的字段（不用时间格式的字段），搜索框会出现在上侧
    search_fields = ['title', 'authors','publisher','publishDate','pages','category','lables']
    # 设置可以在列表中直接修改的字段
    list_editable = ['name','title', 'authors','publisher','ISBN','category','pages','price','buy_order','buy_price','buy_amt','buy_date','publishDate','channel','lables','order','create_user']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    # 配置插件效果
    style_fields = {'introduce': 'ueditor','review': 'ueditor'}
    #设置后台某个字段的排序规则（加负号为倒序）
    ordering = ['-update_time','title']
    #在编辑页面的只读字段
    readonly_fields=[]
    #在列表页显示详情信息
    show_detail_fileds=[]
    # 导出类型 list_export设置为None来禁用数据导出功
    list_export = ('xls', 'xml', 'json','csv')
    #设置默认可编辑字段
    list_display_links=['title','name']
    # 导出字段
    list_export_fields = ['title','name', 'authors','publisher','publishDate','pages','order','category']
    # 导入导出配置，此处也可以只配置一个导入功能或导出功能，而把另一个功能关掉
    import_export_args = {"import_resource_class": BookResource,
                          "export_resource_class": BookResource}

xadmin.site.register(Book,BookAdmin)

# 出版社自定义管理页面
class PublisherAdmin(object):

    model_icon = 'fa fa-book'

    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name','name_pinyin', 'addr','order','create_user','create_time','update_time']

    list_editable = [ 'name', 'addr','order','create_user']

    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['name', 'addr']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['name']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['name']
    ordering = ['order','-create_time','name']
    import_export_args = {"import_resource_class": PublisherResource,
                          "export_resource_class": PublisherResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
xadmin.site.register(Publisher,PublisherAdmin)

# 作者自定义管理页面
class AuthorAdmin(object):
    model_icon='fa fa-user'
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name', 'name_en','name_pinyin','image_img', 'display_name','country','books','dynasty','times','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['name', 'country','times','books','dynasty']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['name', 'country','times','books','dynasty']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['name']
    ordering = ['name','order','-create_time','name']
    list_editable = [ 'name', 'name_en','country','gender','dynasty','times','create_user']
    import_export_args = {"import_resource_class": AuthorResource,
                          "export_resource_class": AuthorResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id



xadmin.site.register(Author,AuthorAdmin)

