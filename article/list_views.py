#coding:utf-8
from django.shortcuts import render
from .models import ArticleColumn,ArticlePost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #分页
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import  HttpResponse


#根据username决定显示所有文章还是个人名下文章
def article_titles(request,username=None):
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


#文章详情
def article_detail(request,id,slug):
    article =get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/list/article_detail.html",{"article":article})

#文章点赞
@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == "like":   #点赞
                article.users_like.add(request.user)#该用户点赞了该文章
                return HttpResponse("1")
            else:#踩你
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")



