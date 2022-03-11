from django.db import models
from base.models import Country,CLC,Category,Dynasty,Times
from django.contrib.auth.models import AbstractUser
from uuslug import slugify
from bms import settings
from django.utils.html import format_html
from stdimage import StdImageField
GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

CHANNEL_CHOICES = (
        ("京东商城", u"京东商城"),
        ("当当网", u"当当网")
    )

# 出版社类
class Publisher(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=100,null=True,blank=True,unique=True)
    name_pinyin=models.SlugField('名称拼音',max_length=300,null=True,blank=True)
    addr = models.CharField('地址', max_length=64,null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True,auto_now=True)
    #create_user=models.IntegerField('创建人',default=1, null=True,blank=True)

    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    # 字符串的友好展示, 在交互式环境测试的时候生效
    def __repr__(self):
        return '<Publisher: %s>' % (self.title)

    # 字符串友好展示，在后台管理的时候生效
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.name_pinyin=slugify(self.name)
        super().save(*args,**kwargs)

    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "出版社"
        # 后台管理显示（复数）
        verbose_name_plural = "出版社"
# 书籍的类
class Book(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name= models.CharField('书名',max_length=200,null=True,blank=True)
    title = models.CharField('书名全',max_length=200,null=True,blank=True)
    title_en=models.CharField('英文书名',max_length=200,null=True,blank=True)
    authors = models.ManyToManyField('Author',verbose_name='作者/编者',related_name='book2authors',blank=True)  # 多对多

    publishDate = models.DateField('出版时间', null=True, blank=True)
    publisher = models.ForeignKey('Publisher', verbose_name='出版社',on_delete=models.CASCADE,null=True,blank=True)  # 一对多
    price = models.DecimalField('定价',max_digits=10, decimal_places=2,null=True,blank=True)  # 最大 999.99
    buy_price = models.DecimalField('购买价格', max_digits=10, decimal_places=2, null=True, blank=True)  # 最大 999.99
    buy_amt = models.DecimalField('买入数量',max_digits=10, decimal_places=2,default=1)  # 最大 999.99
    buy_date = models.DateField('买入日期', null=True, blank=True)
    buy_order = models.CharField('订单号', max_length=200, null=True, blank=True)

    channel = models.CharField('购买渠道', choices=CHANNEL_CHOICES, default='当当网', max_length=32, null=True, blank=True)
    URL = models.CharField('URL', max_length=200, null=True, blank=True)
    ISBN=models.CharField('ISBN',max_length=32,null=True,blank=True)
    category=models.ForeignKey('base.Category',verbose_name='图书分类',on_delete=models.CASCADE,null=True,blank=True)
    product_id=models.CharField('商品编码',max_length=32,null=True,blank=True)
    pages = models.IntegerField('页数', default=0,null=True,blank=True)
    translator = models.ManyToManyField('Author',verbose_name='译者',related_name='book2translator',blank=True)  # 多对多
    amount = models.IntegerField('套装数量', default=1,null=True,blank=True)
    clc=models.ForeignKey('base.CLC',verbose_name='中图分类',on_delete=models.CASCADE,null=True,blank=True)
    imgsrc = models.ImageField(upload_to='static/images/books', default='default.jpeg', verbose_name=u"图片封面",null=True,blank=True)
    image =  StdImageField(upload_to='static/images/books', blank=True, variations={'thumbnail': (100, 75)},  verbose_name=u'图片封面' )
    pack=models.CharField('包装',max_length=32,null=True,blank=True,default='平装')
    size=models.CharField('开本',max_length=32,null=True,blank=True,default='16开')
    words=models.CharField('字数',max_length=32,null=True,blank=True)
    lables=models.CharField('标签',max_length=100,null=True,blank=True)
    introduce=models.TextField('内容简介',null=True,blank=True)
    review=models.TextField('书评',null=True,blank=True)
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True,auto_now=True)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)
    # 字符串的友好展示, 在交互式环境测试的时候生效
    def __repr__(self):
        return '<Book: %s>' % (self.title)

    # 字符串友好展示，在后台管理的时候生效
    def __str__(self):
        return self.name

    def image_img(self):
        if self.imgsrc:
            href = self.imgsrc.url
            src = self.imgsrc.url
            image_html = '<a href="%s" target="_blank" title="照片"> <img alt="" src="%s" />' % (href, src)
            return format_html(image_html, self.imgsrc, )
        else:
            return ""

    def image_img2(self):
        return u'<img src="%s" />' % (self.image.thumbnail.url)
        if self.imgsrc:
            href = self.imgsrc.url
            src = self.imgsrc.url
            image_html = '<a href="%s" target="_blank" title="照片"> <img alt="" src="%s" />' % (href, src)
            return format_html(image_html, self.imgsrc, )
        else:
            return ""
    # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "图书"
        # 后台管理显示（复数）
        verbose_name_plural = "图书"
# 作者的类
class Author(models.Model):
    id = models.AutoField(verbose_name='序号', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=64)
    name_en = models.CharField(verbose_name='英文名字', max_length=64,null=True,blank=True)
    name_pinyin=models.SlugField('名称拼音',max_length=300,null=True,blank=True)
    display_name=models.CharField('显示名称',max_length=300,null=True,blank=True)

    country = models.ForeignKey('base.Country',verbose_name='国家',on_delete=models.CASCADE,default=1,max_length=64,null=True,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male", verbose_name="性别")
    times = models.ForeignKey('base.Times',verbose_name='年代',on_delete=models.CASCADE, default=0,null=True,blank=True)
    dynasty = models.ForeignKey('base.Dynasty',verbose_name='朝代', on_delete=models.CASCADE,default=0,null=True,blank=True)
    imgsrc = models.ImageField(upload_to='static/images/authors', verbose_name=u"图片封面",null=True,blank=True)
    image =  StdImageField(upload_to='static/images/authors', blank=True, variations={'thumbnail': (100, 75)},  verbose_name=u'图片封面' )
    introduce = models.TextField(verbose_name='简介', null=True,blank=True)
    books = models.ManyToManyField(to=Book,related_name='author2books',verbose_name='作品',blank=True)
    # 字符串友好展示，在后台管理的时候生效
    order = models.IntegerField('排序', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', null=True, blank=True,auto_now_add=True)
    update_time = models.DateTimeField('更新时间', null=True, blank=True, auto_now=True)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='创建人', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.country.__str__()=='[中]':
            if self.dynasty is not None:
                return self.name+""+self.dynasty.__str__()
        elif self.country is not None:
            return self.name+""+self.country.__str__()
        return self.name

    def save(self,*args,**kwargs):
        self.name_pinyin=slugify(self.name)
        #self.display_name=self.__str__()
        super().save(*args,**kwargs)

    def image_img(self):
        if self.imgsrc:
            href =self.imgsrc.url
            src =self.imgsrc.url
            image_html='<a href="%s" target="_blank" title="照片"> <img alt="" src="%s" />'%(href,src)
            return format_html(image_html,self.imgsrc,)
        else:
            return ""

    def image_img2(self):
        return u'<img src="%s" />' % (self.image.thumbnail.url)
        if self.imgsrc:
            href =self.imgsrc
            src =self.imgsrc.url
            image_html='<a href="%s" target="_blank" title="照片"> <img alt="" src="%s" />'%(href,src)
            return format_html(image_html,self.imgsrc,)
        else:
            return ""
   # 自定义对应的表名，默认表名：bookApp_book
    class Meta:
        #db_table = "books"
        # 后台管理显示（单数）
        verbose_name = "作者"
        # 后台管理显示（复数）
        verbose_name_plural = "作者"

