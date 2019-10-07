#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserForm,UserInfoForm


from django.contrib.auth.decorators import  login_required
from  .models import UserInfo,UserProfile
from django.contrib.auth.models import  User

from django.utils.translation import ugettext as _
from django.conf import settings
from django.urls import resolvers,reverse


# Create your views here.


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd=login_form.cleaned_data
            user=authenticate(username=cd["username"],password=cd["password"])
            if user:
                login(request,user)
               # return HttpResponse(_("wellcome you.You have been authenticaated successfully"))
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                return HttpResponse(_("sorry,your username or password is not right"))
        else:
            return  HttpResponse(_("Invalid login"))

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
            #return HttpResponse(_("success"))
            #return HttpResponseRedirect(settings.LOGIN_URL)
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponse(_("sorry,you can not register"))
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{"form":user_form,"profile":userprofile_form})


#展示个人信息
@login_required(login_url='/account/login') #只有登录的用户才能看到自己的个人信息，没有登陆的用户转到登录界面
def myself(request):
    user =User.objects.get(username=request.user.username)
    userprofile =UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,"account/myself.html",{"user":user,"userinfo":userinfo,"userprofile":userprofile})


#编辑个人信息
@login_required(login_url='/account/login')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile =UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)

    if request.method =="POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form =UserInfoForm(request.POST)

        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])

            user.email = user_cd['email']
            userprofile.birth =userprofile_cd['birth']
            userprofile.phone =userprofile_cd['phone']
            userinfo.school =userinfo_cd['school']
            userinfo.company =userinfo_cd['company']
            userinfo.address =userinfo_cd['address']
            userinfo.aboutme =userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()

            return HttpResponseRedirect('/account/my-information/')
    else:
        user_form =UserForm(instance=request.user)
        userprofile_form =UserProfileForm(initial={"birth":userprofile.birth,"phone":userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school":userinfo.school,"company":userinfo.company,"address":userinfo.address,"aboutme":userinfo.aboutme})

        return render(request,"account/myself_edit.html",{"user_form":user_form,"userprofile_form":userprofile_form,"userinfo_form":userinfo_form})


#编辑图像，实现裁剪与上传
@login_required(login_url='/account/login')
def my_image(request):
    if request.method =="POST":
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request,'account/imagecrop.html')


