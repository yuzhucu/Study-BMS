from .models import Country,Category,Times,Dynasty,CLC
from user.models import UserProfile
from .resources import CLCResource,DynastyResource,CategoryResource,CountryResource,TimesResource
import xadmin
from xadmin import views
from django.apps import apps
from django.utils.encoding import force_text, smart_text, smart_str
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from xadmin.views.base import filter_hook
from collections import OrderedDict
from xadmin.util import static, json, vendor, sortkeypicker
class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题
    user_themes= [
        {
            "name": "Cerulean",
            "description": "A calm blue sky",
            "thumbnail": "https://bootswatch.com/cerulean/thumbnail.png",
            "preview": "https://bootswatch.com/cerulean/",
            "css": "https://bootswatch.com/5/cerulean/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/cerulean/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/cerulean/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/cerulean/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/cerulean/_variables.scss"
        },
        {
            "name": "Cosmo",
            "description": "An ode to Metro",
            "thumbnail": "https://bootswatch.com/cosmo/thumbnail.png",
            "preview": "https://bootswatch.com/cosmo/",
            "css": "https://bootswatch.com/5/cosmo/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/cosmo/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/cosmo/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/cosmo/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/cosmo/_variables.scss"
        },
        {
            "name": "Cyborg",
            "description": "Jet black and electric blue",
            "thumbnail": "https://bootswatch.com/cyborg/thumbnail.png",
            "preview": "https://bootswatch.com/cyborg/",
            "css": "https://bootswatch.com/5/cyborg/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/cyborg/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/cyborg/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/cyborg/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/cyborg/_variables.scss"
        },
        {
            "name": "Darkly",
            "description": "Flatly in night mode",
            "thumbnail": "https://bootswatch.com/darkly/thumbnail.png",
            "preview": "https://bootswatch.com/darkly/",
            "css": "https://bootswatch.com/5/darkly/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/darkly/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/darkly/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/darkly/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/darkly/_variables.scss"
        },
        {
            "name": "Flatly",
            "description": "Flat and modern",
            "thumbnail": "https://bootswatch.com/flatly/thumbnail.png",
            "preview": "https://bootswatch.com/flatly/",
            "css": "https://bootswatch.com/5/flatly/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/flatly/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/flatly/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/flatly/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/flatly/_variables.scss"
        },
        {
            "name": "Journal",
            "description": "Crisp like a new sheet of paper",
            "thumbnail": "https://bootswatch.com/journal/thumbnail.png",
            "preview": "https://bootswatch.com/journal/",
            "css": "https://bootswatch.com/5/journal/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/journal/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/journal/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/journal/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/journal/_variables.scss"
        },
        {
            "name": "Litera",
            "description": "The medium is the message",
            "thumbnail": "https://bootswatch.com/litera/thumbnail.png",
            "preview": "https://bootswatch.com/litera/",
            "css": "https://bootswatch.com/5/litera/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/litera/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/litera/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/litera/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/litera/_variables.scss"
        },
        {
            "name": "Lumen",
            "description": "Light and shadow",
            "thumbnail": "https://bootswatch.com/lumen/thumbnail.png",
            "preview": "https://bootswatch.com/lumen/",
            "css": "https://bootswatch.com/5/lumen/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/lumen/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/lumen/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/lumen/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/lumen/_variables.scss"
        },
        {
            "name": "Lux",
            "description": "A touch of class",
            "thumbnail": "https://bootswatch.com/lux/thumbnail.png",
            "preview": "https://bootswatch.com/lux/",
            "css": "https://bootswatch.com/5/lux/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/lux/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/lux/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/lux/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/lux/_variables.scss"
        },
        {
            "name": "Materia",
            "description": "Material is the metaphor",
            "thumbnail": "https://bootswatch.com/materia/thumbnail.png",
            "preview": "https://bootswatch.com/materia/",
            "css": "https://bootswatch.com/5/materia/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/materia/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/materia/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/materia/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/materia/_variables.scss"
        },
        {
            "name": "Minty",
            "description": "A fresh feel",
            "thumbnail": "https://bootswatch.com/minty/thumbnail.png",
            "preview": "https://bootswatch.com/minty/",
            "css": "https://bootswatch.com/5/minty/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/minty/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/minty/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/minty/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/minty/_variables.scss"
        },
        {
            "name": "Morph",
            "description": "A neumorphic layer",
            "thumbnail": "https://bootswatch.com/morph/thumbnail.png",
            "preview": "https://bootswatch.com/morph/",
            "css": "https://bootswatch.com/5/morph/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/morph/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/morph/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/morph/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/morph/_variables.scss"
        },
        {
            "name": "Pulse",
            "description": "A trace of purple",
            "thumbnail": "https://bootswatch.com/pulse/thumbnail.png",
            "preview": "https://bootswatch.com/pulse/",
            "css": "https://bootswatch.com/5/pulse/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/pulse/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/pulse/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/pulse/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/pulse/_variables.scss"
        },
        {
            "name": "Quartz",
            "description": "A glassmorphic layer",
            "thumbnail": "https://bootswatch.com/quartz/thumbnail.png",
            "preview": "https://bootswatch.com/quartz/",
            "css": "https://bootswatch.com/5/quartz/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/quartz/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/quartz/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/quartz/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/quartz/_variables.scss"
        },
        {
            "name": "Sandstone",
            "description": "A touch of warmth",
            "thumbnail": "https://bootswatch.com/sandstone/thumbnail.png",
            "preview": "https://bootswatch.com/sandstone/",
            "css": "https://bootswatch.com/5/sandstone/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/sandstone/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/sandstone/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/sandstone/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/sandstone/_variables.scss"
        },
        {
            "name": "Simplex",
            "description": "Mini and minimalist",
            "thumbnail": "https://bootswatch.com/simplex/thumbnail.png",
            "preview": "https://bootswatch.com/simplex/",
            "css": "https://bootswatch.com/5/simplex/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/simplex/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/simplex/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/simplex/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/simplex/_variables.scss"
        },
        {
            "name": "Sketchy",
            "description": "A hand-drawn look for mockups and mirth",
            "thumbnail": "https://bootswatch.com/sketchy/thumbnail.png",
            "preview": "https://bootswatch.com/sketchy/",
            "css": "https://bootswatch.com/5/sketchy/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/sketchy/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/sketchy/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/sketchy/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/sketchy/_variables.scss"
        },
        {
            "name": "Slate",
            "description": "Shades of gunmetal gray",
            "thumbnail": "https://bootswatch.com/slate/thumbnail.png",
            "preview": "https://bootswatch.com/slate/",
            "css": "https://bootswatch.com/5/slate/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/slate/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/slate/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/slate/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/slate/_variables.scss"
        },
        {
            "name": "Solar",
            "description": "A spin on Solarized",
            "thumbnail": "https://bootswatch.com/solar/thumbnail.png",
            "preview": "https://bootswatch.com/solar/",
            "css": "https://bootswatch.com/5/solar/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/solar/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/solar/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/solar/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/solar/_variables.scss"
        },
        {
            "name": "Spacelab",
            "description": "Silvery and sleek",
            "thumbnail": "https://bootswatch.com/spacelab/thumbnail.png",
            "preview": "https://bootswatch.com/spacelab/",
            "css": "https://bootswatch.com/5/spacelab/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/spacelab/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/spacelab/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/spacelab/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/spacelab/_variables.scss"
        },
        {
            "name": "Superhero",
            "description": "The brave and the blue",
            "thumbnail": "https://bootswatch.com/superhero/thumbnail.png",
            "preview": "https://bootswatch.com/superhero/",
            "css": "https://bootswatch.com/5/superhero/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/superhero/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/superhero/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/superhero/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/superhero/_variables.scss"
        },
        {
            "name": "United",
            "description": "Ubuntu orange and unique font",
            "thumbnail": "https://bootswatch.com/united/thumbnail.png",
            "preview": "https://bootswatch.com/united/",
            "css": "https://bootswatch.com/5/united/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/united/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/united/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/united/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/united/_variables.scss"
        },
        {
            "name": "Vapor",
            "description": "A cyberpunk aesthetic",
            "thumbnail": "https://bootswatch.com/vapor/thumbnail.png",
            "preview": "https://bootswatch.com/vapor/",
            "css": "https://bootswatch.com/5/vapor/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/vapor/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/vapor/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/vapor/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/vapor/_variables.scss"
        },
        {
            "name": "Yeti",
            "description": "A friendly foundation",
            "thumbnail": "https://bootswatch.com/yeti/thumbnail.png",
            "preview": "https://bootswatch.com/yeti/",
            "css": "https://bootswatch.com/5/yeti/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/yeti/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/yeti/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/yeti/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/yeti/_variables.scss"
        },
        {
            "name": "Zephyr",
            "description": "Breezy and beautiful",
            "thumbnail": "https://bootswatch.com/zephyr/thumbnail.png",
            "preview": "https://bootswatch.com/zephyr/",
            "css": "https://bootswatch.com/5/zephyr/bootstrap.css",
            "cssMin": "https://bootswatch.com/5/zephyr/bootstrap.min.css",
            "cssCdn": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/zephyr/bootstrap.min.css",
            "scss": "https://bootswatch.com/5/zephyr/_bootswatch.scss",
            "scssVariables": "https://bootswatch.com/5/zephyr/_variables.scss"
        }
    ]
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "图书后台管理系统"  # 设置站点标题
    site_footer = "yuzhucu的图书馆"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠，在左侧，默认的
    # 设置models的全局图标, UserProfile, Sports 为表名
    #global_search_models = [UserProfile, Sports]
    global_models_icon = {'publisher':'fa fa-bank'}
    apps_icons = { 'base': "fa fa-folder-open",
                   'order': "fa fa-shopping-cart",
                   'book': "fa fa-book",
                   'user': "fa fa-user"

                   }

    global_models_icon = {
        UserProfile: "glyphicon glyphicon-user"}

    @filter_hook
    def get_nav_menu(self):
        site_menu = list(self.get_site_menu() or [])
        had_urls = []

        def get_url(menu, had_urls):
            if 'url' in menu:
                had_urls.append(menu['url'])
            if 'menus' in menu:
                for m in menu['menus']:
                    get_url(m, had_urls)

        get_url({'menus': site_menu}, had_urls)

        nav_menu = OrderedDict()

        menus_ = self.admin_site._registry.items()
        for model, model_admin in menus_:
            if getattr(model_admin, 'hidden_menu', False):
                continue
            app_label = model._meta.app_label
            app_icon = None
            model_dict = {
                'title': smart_text(capfirst(model._meta.verbose_name_plural)),
                'url': self.get_model_url(model, "changelist"),
                'icon': self.get_model_icon(model),
                'perm': self.get_model_perm(model, 'view'),
                'order': model_admin.order,
            }
            if model_dict['url'] in had_urls:
                continue

            app_key = "app:%s" % app_label
            if app_key in nav_menu:
                nav_menu[app_key]['menus'].append(model_dict)
            else:
                # Find app title
                app_title = smart_text(app_label.title())
                if app_label.lower() in self.apps_label_title:
                    app_title = self.apps_label_title[app_label.lower()]
                else:
                    appL = apps.get_app_config(app_label)
                    app_title = smart_text(apps.get_app_config(app_label).verbose_name)
                    # added by Fiona for menu ordering
                    if app_label == "auth":
                        app_index = len(menus_) - 1
                    elif app_label == "xadmin":
                        app_index = len(menus_) - 2
                    else:
                        app_index = appL.orderIndex
                # find app icon
                if app_label.lower() in self.apps_icons:
                    app_icon = self.apps_icons[app_label.lower()]
                nav_menu[app_key] = {
                    "orderIndex": app_index,
                    'title': app_title,
                    'menus': [model_dict],
                }
            app_menu = nav_menu[app_key]
            if app_icon:
                app_menu['first_icon'] = app_icon
            elif ('first_icon' not in app_menu or
                  app_menu['first_icon'] == self.default_model_icon) and model_dict.get('icon'):
                app_menu['first_icon'] = model_dict['icon']

            if 'first_url' not in app_menu and model_dict.get('url'):
                app_menu['first_url'] = model_dict['url']

        for menu in nav_menu.values():
            menu['menus'].sort(key=sortkeypicker(['order', 'title']))

        nav_menu = list(nav_menu.values())
        # nav_menu.sort(key=lambda x: x['title'])
        # 左侧菜单自定义排序新增
        nav_menu.sort(key=sortkeypicker(['orderIndex']))
        site_menu.extend(nav_menu)
        return site_menu

    #UserProfile: "glyphicon glyphicon-user", Sports: "fa fa-cloud"
xadmin.site.register(views.CommAdminView, GlobalSettings)

# 国家码表
class CountryAdmin(object):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'country','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'country']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'country']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['country']
    list_editable = ['country','tag','order','create_user']
    import_export_args = {"import_resource_class": CountryResource,
                          "export_resource_class": CountryResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
xadmin.site.register(Country,CountryAdmin)

class CategoryAdmin(object):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'category','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'category']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'category']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['category']
    list_editable = ['category','tag','order','create_user']
    import_export_args = {"import_resource_class": CategoryResource,
                          "export_resource_class": CategoryResource}
    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
xadmin.site.register(Category,CategoryAdmin)

class CLCAdmin(object):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'code','name','level','parent_code','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'code','name','level','parent_code']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'code','name','level','parent_code']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['name']
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
xadmin.site.register(CLC,CLCAdmin)

class TimesAdmin(object):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'times','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'times']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'times']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['times']
    list_editable = ['times','tag','order','create_user']
    import_export_args = {"import_resource_class": TimesResource,
                          "export_resource_class": TimesResource}

    def instance_forms(self):
        super().instance_forms()
        # 判断是否为新建操作，新建操作才会设置creator的默认值
        if not self.org_obj:
            self.form_obj.initial['create_user'] = self.request.user.id
xadmin.site.register(Times,TimesAdmin)

class DynastyAdmin(object):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'dynasty','tag','order','create_user','create_time','update_time']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['id', 'dynasty']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['id', 'dynasty']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 20
    list_display_links=['dynasty']
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
xadmin.site.register(Dynasty,DynastyAdmin)
