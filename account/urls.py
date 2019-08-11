#coding:utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/', views.user_login,name="user_login"),#自定义登录
    url(r'^logout/', views.user_logout,name="user_logout"),#自定义退出
    url(r'^register/',views.register,name="user_register"),#自定义注册

    url(r'^my-information/$',views.myself,name='my_information'), #展示个人信息
    url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),  #编辑个人信息

    url(r'^my-image/$',views.my_image,name='my_image'), #头像






]

