from .models import Book,Publisher,Author
from base.models import Category,Country,CLC,Dynasty

def book_context(request):
    """这里写需要的全局变量，直接返回querydict，方便取数据"""
    category = Category.objects.all().order_by('order')
    publishers = Publisher.objects.all().order_by('name_pinyin')
    authors = Author.objects.all().order_by('name_pinyin')

    context = {
     "category": category,
     "publishers": publishers,
     "authors": authors,
     }
    return context
