#coding:utf-8

from django.urls import  path
from django.conf.urls import  url
from . import  views

urlpatterns =[
    path('list-images/',views.list_images,name="list_images"), #展示图片
    path('images/',views.falls_images,name="fall_images"),#瀑布流展示图片
    url(r'^upload-image/$', views.upload_image, name="upload_image"),#搜集图片
    path('del-image/',views.del_images,name="del_image"),#删除图片
]
