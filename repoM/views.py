from django.shortcuts import render,redirect,HttpResponse
from .models import SystemConfig,CodeRepo
from copy import deepcopy
from .gitlab import Gitlab

# Create your views here.
def repo(request):
    return render(request,'repo/repo.html',locals())

def addrepo(request):
    return HttpResponse("敬请期待")


def importrepo(request):
    sys_list = SystemConfig.objects.filter(sys_type='git')
    if request.method == 'POST':
        message="仓库导入只支持 GitLab 仓库"
        sys_id = request.POST['sys_choice']
        print(sys_id)
        try:
            sys_obj = SystemConfig.objects.get(id=sys_id)
            print("test")
            repo_list = Gitlab(sys_obj.sys_api_url,sys_obj.sys_privatetoken).projects
            print("test2")
            print(repo_list)
            repo_id_list = [repo_id['repo_id'] for repo_id in CodeRepo.objects.filter(repo_system=sys_id).values('repo_id')] 
            #TODO 路径和Token 验证
            
            import_count = 0
            for repo in repo_list:
                repo["repo_system"]=sys_id
                # 查询所选 system 所有的 repo_id,判断是否已存在.
                if repo["repo_id"] in repo_id_list:
                    print("项目已存在")
                    continue
                print("test3")    
                CodeRepo.objects.create(**repo)
        except:
            message="导入失败"
            return render(request,'repo/importrepo.html',locals())
    return render(request,'repo/importrepo.html',locals())

def systemconfig(request):
    systemconfig_obj = SystemConfig.objects.all()
    return render(request,'systemconfig.html',locals())


def editsystemconfig(request,system_id):
    try:
        systemconfig_obj = SystemConfig.objects.get(id=system_id)
    except:
        message = '该项不存在'
        return redirect('/repoM/systemconfig/')
    if request.method == 'POST':
        sys_info = deepcopy(request.POST.dict())
        del sys_info['csrfmiddlewaretoken']
        SystemConfig.objects.filter(id=system_id).update(**sys_info)
        return redirect('/repoM/systemconfig/')
    return render(request,'editsystemconfig.html', locals())

def delsystemconfig(request,system_id):
    try:
        systemconfig_obj = SystemConfig.objects.get(id=system_id)
    except:
        message = '该项不存在'
        return redirect('/repoM/systemconfig/')
    SystemConfig.objects.filter(id=system_id).delete()
    return redirect('/repoM/systemconfig/')

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