#coding:utf-8
from django.shortcuts import render
from .models import ArticleColumn,ArticlePost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #分页
from django.shortcuts import get_object_or_404


def article_titles(request):  #显示所有文章
    article_title = ArticlePost.objects.all()

    paginator = Paginator(article_title,8)
    page = request.GET.get('page')#获取GET请求中的page值
    try:
        current_page = paginator.page(page)#得到指定页面内容
        articles = current_page.object_list #得到该页面所有的对象列表
    except PageNotAnInteger:
        current_page = paginator.page(1)#得到指定页面内容
        articles = current_page.object_list #得到该页面所有的对象列表
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)#得到指定页面内容
        articles = current_page.object_list #得到该页面所有的对象列表

    return render(request,"article/list/article_titles.html",{"articles":articles,"page":current_page})

def article_detail(request,id,slug):  #文章详情
    article =get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/list/article_detail.html",{"article":article})



