#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from . forms import LoginForm,RegistrationForm,UserProfileForm

from django.contrib.auth.decorators import  login_required
from  .models import UserInfo,UserProfile
from django.contrib.auth.models import  User

# Create your views here.


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd["username"],password=cd["password"])
            if user:
                login(request,user)
                return HttpResponse("wellcome you.You have been authenticaated successfully")
            else:
                return HttpResponse("sorry,your username or password is not right")
        else:
            return  HttpResponse("Invalid login")

    if request.method == "GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})


def user_logout(request):
    return render(request,"account/logout.html")


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False) #将表单数据生成该数据对象，但因为“False”还没保存到数据库
            new_user.set_password (user_form.cleaned_data["password"])
            new_user.save() #保存到数据库

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)  #保存用户祖册信息的同时，在account_userinfo表写入用户数据
            UserProfile.objects.create(user=new_user)
            return HttpResponse("success")
        else:
            return HttpResponse("sorry,you can not register")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{"form":user_form,"profile":userprofile_form})



@login_required(login_url='/account/login') #只有登录的用户才能看到自己的个人信息，没有登陆的用户转到登录界面
def myself(request):
    user =User.objects.get(username=request.user.username)
    userprofile =UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,"account/myself.html",{"user":user,"userinfo":userinfo,"userprofile":userprofile})


