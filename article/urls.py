#coding:utf-8

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('article-column/', views.article_column, name="article_column"),  #栏目
    path('rename-column/', views.rename_article_column, name="rename_article_column"),  #编辑栏目
    path('del-column/', views.del_article_column, name="del_article_column"),#删除栏目

    path('article_post/', views.article_post, name="article_post"),#发布文章
    path('article_list/', views.article_list, name="article_list"),#显示文章列表
    path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),#查看文章
    path('del-article/', views.del_article, name="del_article"),#删除文章
    #path('redit-article/(?P<article_id>\d+)/$', views.redit_article, name="redit_article"),#修改文章
    path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
]