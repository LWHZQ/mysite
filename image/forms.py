#coding:utf-8

from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from .models import  Image
import urllib,requests
from urllib import request


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')

    def clean_url(self): #检验某个字段
        url = self.cleaned_data['url']  #self.clean_data获取请求数据
        valid_extensions =['jpg','jpeg','png','gif']
        extention = url.rsplit('.',1)[1].lower()
        print("extention:%s" %extention)

        if extention not in valid_extensions:
            raise forms.ValidationError("所给的url不符合图片扩展名")
        return url

    def save(self, force_insert=False,force_update=False, commit=True):
        image = super(ImageForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{0}.{1}'.format(slugify(image.title),image.url.rsplit('.',1)[1].lower()) #以输入的title作为图片名称
        print("image_name:%s" %image_name)

        response =request.urlopen(image_url)
        html = response.read()
        print(" html:%s" %html)
        image.image.save(image_name,ContentFile(html),save=False)
        if commit:
            image.save()
        return image

