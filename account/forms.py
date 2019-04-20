#coding:utf-8

from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.models import  User#引入Django默认的用户模型User类

from .models import  UserProfile #增加User模型中没有的字段

#登录用户的表单类
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

#注册用户的表单类
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise  forms.ValidationError('password do not match')
        return cd['password2']


#为注册用户增加额外字段
class UserProfileForm(forms.ModelForm):
    class Meta:
        model =UserProfile
        fields = ("phone","birth")
