#coding:utf-8


from django import  forms
from .models import ArticleColumn,ArticlePost

#文章栏目表单类
class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)

#发布与显示文章表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost  #说明表单中各个字段来源
        fields = ("title","body")  #本表单类中用到的字段