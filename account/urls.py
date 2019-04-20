#coding:utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/', views.user_login,name="user_login"),#自定义登录
    url(r'^logout/', views.user_logout,name="user_logout"),#自定义退出



]

