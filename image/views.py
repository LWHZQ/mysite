#coding:utf-8
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Image
from .forms import ImageForm


#接受并处理前端提交的数据
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({'status':"1"})
        except:
            return JsonResponse({'status':"0"})
    else:
        print('*'*20)
        return JsonResponse({'status':"0"})

#展示个人名下图片
@login_required(login_url='/account/login/')
def list_images(request):
    images = Image.objects.filter(user=request.user)
    print("images:%s" %images)
    return render(request,'image/list_images.html',{"images":images})

#删除图片
@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def del_images(request):
    image_id = request.POST['image_id']
    try:
        Image.objects.get(id=image_id).delete()
        return JsonResponse({'status':"1"})
    except:
        return JsonResponse({'status':"2"})

#瀑布流方式展示all图片
def falls_images(request):
    images = Image.objects.all()
    return render(request,"image/falls_images.html",{"images":images})

