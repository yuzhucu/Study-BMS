from django.shortcuts import render, redirect
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage
# Create your views here.
from book import models,forms
from book.forms import BookForm,AuthorForm,PublisherForm
from django.db.models import Q
from base.common import Pagination
# 出版社列表
def index(request):
    # 查询
    # 渲染
    return render(request, 'home.html')

# 出版社列表
def publisher_list(request):
    # 查询
    publisher = models.Publisher.objects.all().order_by('-update_time') # ORM中的查询全部
    # 渲染
    return render(request, 'pub_list.html', {'publisher_list': publisher})

# 添加出版社
def publisher_add(request):
    # POST请求表示用户已提交数据
    if request.method == 'POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pub/list/')
        else:
            publisher = models.Publisher.objects.filter(pk=id).first()
            form = PublisherForm(request.POST, instance=publisher)
            return render(request, 'pub_add.html', locals())

    # 渲染待添加页面给用户
    form = PublisherForm()
    return render(request, 'pub_add.html', locals())

# 编辑出版社
def publisher_edit(request):
    id = request.GET.get('id')
    publisher = models.Publisher.objects.filter(pk=id).first()
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('/pub/list/')
        else:
            publisher = models.Publisher.objects.filter(pk=id).first()
            form = PublisherForm(request.POST, instance=publisher)
            return render(request, 'pub_edit.html', locals())
        # 注意保存
        #return redirect('/pub/list/')

    form=PublisherForm(instance=publisher)
    return render(request, 'pub_edit.html', locals())

# 删除出版社
def publisher_del(request):
    # GET请求拿到url中的ID
    drop_id = request.GET.get('id')
    drop_obj = models.Publisher.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/pub/list/')

# 书籍的列表
def book_list(request):
    book = models.Book.objects.order_by('-update_time').all()
    #分页器： 参数1：要分页的数据；参数2：设置每页要展示的数据个数；参数3：如果最后一页不到5个数据，是否将最后一页的数据合并到上一页进行展示；默认是False，不合并；
    paginator=Paginator(book,20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'book_list.html', {'book_list': book,'page':page})

# 添加本书籍
def book_add(request):
    if request.method == 'POST':
       form =BookForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/book/list/')
       else:
           book = models.Book.objects.filter(pk=id).first()
           form = BookForm(request.POST, instance=book)
           return render(request, 'book_add.html', locals())

    form =BookForm()
    return render(request,'book_add.html',locals())

# 编辑本书籍
def book_edit(request):
    id=request.GET.get('id')
    book = models.Book.objects.filter(pk=id).first()
    if request.method == 'POST':
        form =BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/book/list/')
        else:
            book = models.Book.objects.filter(pk=id).first()
            form = BookForm(request.POST, instance=book)
            return render(request,'book_edit.html',locals())


    form=BookForm(instance=book)
    return render(request,'book_edit.html',locals())

# 删除本书籍
def book_del(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Book.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/book/list/')

# 作者的列表
def author_list(request):
    author = models.Author.objects.all().order_by('-update_time')
    return render(request, 'author_list.html', {'author_list': author})

# 添加作者
def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/list/')
        else:
            author = models.Author.objects.filter(pk=id).first()
            form = AuthorForm(request.POST, instance=author)
            return render(request, 'author_add.html', locals())
    form = AuthorForm()
    return render(request, 'author_add.html', locals())

# 修改作者
def author_edit(request):
    id = request.GET.get('id')
    author = models.Author.objects.filter(pk=id).first()
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/author/list/')
        else:
            author = models.Book.objects.filter(pk=id).first()
            form = AuthorForm(request.POST, instance=author)
            return render(request, 'author_edit.html', locals())

    form = AuthorForm(instance=author)
    return render(request, 'author_edit.html', locals())

# 删除作者
def author_del(request):
    drop_id = request.GET.get('id')
    drop_obj = models.Author.objects.get(id=drop_id)
    drop_obj.delete()
    return redirect('/author/list/')

def book_search(request):
    search = request.GET.get('q')
    books = models.Book.objects.all().order_by('-update_time')
    if search:
        books=books.filter(
            Q(name__icontains=search)| Q(category__category__icontains=search) |
            Q(publisher__name__icontains=search) | Q(authors__name__icontains=search) |
            Q(ISBN__icontains=search) | Q(lables__icontains=search) |Q(introduce__icontains=search)

        ).distinct()

    paginator = Paginator(books, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'book_list.html', {'book_list': books, 'page': page})

def author_search(request):
    search = request.GET.get('q')
    authors = models.Author.objects.all().order_by('-update_time')
    if search:
        authors=authors.filter(
            Q(name__icontains=search)| Q(country__country__icontains=search) |
            Q(times__times__icontains=search) | Q(dynasty__dynasty__icontains=search) |
            Q(books__name__icontains=search) | Q(name_en__icontains=search) |Q(introduce__icontains=search)

        ).distinct()

    paginator = Paginator(authors, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'author_list.html', {'author_list': authors, 'page': page})

def pub_search(request):
    search = request.GET.get('q')
    publishers = models.Publisher.objects.all().order_by('-update_time')
    if search:
        publishers=publishers.filter(
            Q(name__icontains=search)| Q(addr__icontains=search)

        ).distinct()

    paginator = Paginator(publishers, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'pub_list.html', {'publisher_list': publishers, 'page': page})

def get_books_by_category(request,id):
    books = models.Book.objects.filter(category_id=id).order_by('-update_time')
    paginator = Paginator(books, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'category.html', {'book_list': books, 'page': page})


def get_books_by_author(request,id):
    books = models.Book.objects.filter(authors=id).order_by('-update_time')
    paginator = Paginator(books, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'category.html', {'book_list': books, 'page': page})


def get_books_by_publisher(request,id):
    books = models.Book.objects.filter(publisher_id=id).order_by('-update_time')
    paginator = Paginator(books, 20)
    try:
        page_number = request.GET.get('page', '1')
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # 如果出现上述异常，默认展示第1页
        page = paginator.page(1)

    return render(request, 'category.html', {'book_list': books, 'page': page})