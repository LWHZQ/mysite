#coding:utf-8
from django.shortcuts import render
from .models import ArticleColumn,ArticlePost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #分页
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def article_titles(request,username=None):  #根据username决定显示所有文章还是个人名下文章
    if username:
        user = User.objects.get(username=username)
        article_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
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

    if username:
        return render(request,"article/list/author_articles.html",{"articles":articles,"page":current_page,"userinfo":userinfo,"user":user})
    else:
        return render(request,"article/list/article_titles.html",{"articles":articles,"page":current_page})

def article_detail(request,id,slug):  #文章详情
    article =get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/list/article_detail.html",{"article":article})



