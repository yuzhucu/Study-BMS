from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email', 'mobile', 'create_time', ]
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'username']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'username']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links = ['username']
    list_editable = []

    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id

admin.site.register(UserProfile, UserProfileAdmin)

