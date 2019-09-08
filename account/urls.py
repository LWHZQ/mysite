#coding:utf-8
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', views.user_login,name="user_login"),#自定义登录
    url(r'^logout/', views.user_logout,name="user_logout"),#自定义退出
    url(r'^register/',views.register,name="user_register"),#自定义注册

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html", success_url="/account/password-change-done/"), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html", email_template_name="account/password_reset_email.html", success_url='/account/password-reset-done/'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html", success_url='/account/password-reset-complete/'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

    url(r'^my-information/$',views.myself,name='my_information'), #展示个人信息
    url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),  #编辑个人信息

    url(r'^my-image/$',views.my_image,name='my_image'), #头像






]

