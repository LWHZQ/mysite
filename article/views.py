#coding:utf-8
from django.shortcuts import render

# Create your views here.
from .models import  ArticleColumn,ArticlePost
from .forms import ArticleColumnForm,ArticlePostForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.shortcuts import get_object_or_404
from django.http import  HttpResponse

##栏目
@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method == "GET":  #获取栏目
        columns = ArticleColumn.objects.filter(user = request.user)
        column_form = ArticleColumnForm()
        return render(request,'article/column/article_column.html',{"columns":columns,"column_form":column_form})
    if request.method == "POST": #新增栏目
        column_name = request.POST["column"]
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse('1')




@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article_column(request):   #编辑栏目
    column_name = request.POST["column_name"]
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse("0")


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article_column(request):    #删除栏目
    column_id = request.POST["column_id"]
    try:
        line=ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


##文章
@login_required(login_url='/account/login/')
@csrf_exempt
def article_post(request):          #发布文章
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd =article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse(1)
            except Exception as e:
                print(e)
                return HttpResponse(2)
        else:
            return HttpResponse(3)
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request,"article/column/article_post.html",{"article_post_form":article_post_form,"article_columns":article_columns})


@login_required(login_url="/account/login/")
def article_list(request):  #显示文章
    articles = ArticlePost.objects.filter(author=request.user)
    return render(request,"article/column/article_list.html",{"articles":articles})


@login_required(login_url="/account/login/")
def article_detail(request,id,slug):  #文章详情
    article =get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,"article/column/article_detail.html",{"article":article})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article(request):    #删除文章
    article_id = request.POST["article_id"]
    try:
        article=ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required(login_url='/account/login/')
@csrf_exempt
def redit_article(request,article_id):   #编辑文章
    if request.method == "GET":
        article_columns = request.user.article_column.all() #用于显示文章的下拉栏目
        article = ArticlePost.objects.get(id=article_id)  #用于显示文章的body
        this_article_form = ArticlePostForm(initial={"title":article.title})
        this_article_column = article.column   #该文章所属栏目

        return render(request,"article/column/redit_article.html",{"article":article,"article_columns":article_columns,"this_article_form":this_article_form,"this_article_column":this_article_column})
    else:
        redit_article = ArticlePost.objects.get(id=article_id)
        try:
            redit_article.column = request.user.article_column.get(id=request.POST["column_id"])
            redit_article.title = request.POST['title']
            redit_article.body = request.POST["body"]
            redit_article.save()
            return HttpResponse(1)
        except:
            return HttpResponse(2)



