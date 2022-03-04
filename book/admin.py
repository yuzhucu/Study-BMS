from django.contrib import admin
from .models import Book,Publisher,Author
# Register your models here.

# 书籍自定义管理页面
class BookAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name','title','publisher','publishDate','image_img','price','buy_order','buy_price','buy_amt','buy_date','ISBN','category','pages','channel','lables','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['title', 'publisher']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['title']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20

admin.site.register(Book, BookAdmin)

# 出版社自定义管理页面
class PublisherAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name', 'addr']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['name', 'addr']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['name']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
admin.site.register(Publisher, PublisherAdmin)

# 出版社自定义管理页面
class AuthorAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name', 'name_en','name_pinyin', 'image_img','display_name','country','dynasty','times','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['name',]
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['name']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
admin.site.register(Author,AuthorAdmin)

