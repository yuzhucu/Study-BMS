from django import forms
from book import models

class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = "__all__"

        labels = {
            "title": "书名",
            "price": "价格"
        }

        widgets = {

        }

        error_messages ={
            "name": {"required": "不能为空", 'invalid': u'格式错误', 'unique': u'存在相同的数据'},

        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })

class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = "__all__"

        labels = {

        }

        widgets = {

        }

        error_messages ={
            "name": {"required": "不能为空", 'invalid': u'格式错误', 'unique': u'存在相同的数据'},
            "name_pinyin": {"required": "不能为空", 'invalid': u'格式错误', 'unique': u'存在相同的数据'},

        }

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })

class PublisherForm(forms.ModelForm):

    class Meta:
        model = models.Publisher
        fields = "__all__"

        labels = {

        }

        widgets = {

        }

        error_messages ={
            "name": {"required": "不能为空",'invalid': u'格式错误','unique': u'存在相同的数据' },
            "name_pinyin": {"required": "不能为空", 'invalid': u'格式错误', 'unique': u'存在相同的数据'},

        }

    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                    'class': 'form-control'
            })