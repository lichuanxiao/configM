from django.shortcuts import render,redirect,HttpResponse
from .models import SystemConfig
from copy import deepcopy

# Create your views here.

def systemconfig(request):
    if request.method == 'POST':
        return HttpResponse('敬请期待')
    return render(request,'systemconfig.html',locals())


def editsystemconfig(request):
    pass


def addsystemconfig(request):
    if request.method == 'POST':
        sys_info = deepcopy(request.POST.dict())
        sysname = request.POST['sys_name']
        try:
            SystemConfig.objects.get(sys_name=sysname)
            message = "该系统已存在，系统名称不能重复"
            return render(request,'addsystemconfig.html',locals())
        except:
            del sys_info['csrfmiddlewaretoken']
            SystemConfig.objects.create(**sys_info)
            return redirect('/repoM/systemconfig/')
    return render(request,'addsystemconfig.html',locals())