"""bms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from book import views,models
import xadmin
from django.views.static import serve
from bms import settings

xadmin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    #url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', views.book_list),
    url(r'^pub/list/', views.publisher_list),      # 出版社列表
    url(r'^pub/add/', views.publisher_add),     # 新增出版社
    url(r'^pub/edit/', views.publisher_edit),     # 编辑出版社
    url(r'^pub/del/', views.publisher_del),     # 删除出版社
    url(r'^author/list/', views.author_list),     # 作者列表
    url(r'^author/add/', views.author_add),    # 新增作者
    url(r'^author/del/', views.author_del),    # 删除作者
    url(r'^author/edit/', views.author_edit),  # 编辑作者

    url(r'^book/list/', views.book_list),     # 图书列表
    url(r'^book/add', views.book_add),     # 新增图书
    url(r'^book/del/', views.book_del),     # 删除图书
    url(r'^book/edit/', views.book_edit),     # 编辑图书
    url(r'^book/search/', views.book_search),  # 查询图书
    url(r'^pub/search/', views.pub_search),  # 查询图书
    url(r'^author/search/', views.author_search),  # 查询图书
    path('category/<int:id>', views.get_books_by_category,name="category"),  # 查询图书
    path(r'^publisher/<int:id>/', views.get_books_by_publisher,name="publisher"),  # 查询图书
    path(r'^author/<int:id>/', views.get_books_by_author,name="author"),  # 查询图书
    url(r'^/', views.book_list),
    path('', views.book_list),  # 查询图书

    # url(r'^login/', views.login),     # 登录动作
    # url(r'^signup/', views.register),     # 注册页面
    # url(r'^register/', views.register),     # 注册
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),  # 指定上传媒体位置
]