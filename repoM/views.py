from django.shortcuts import render,redirect,HttpResponse
from .models import SystemConfig,CodeRepo
from copy import deepcopy
from .gitlab import Gitlab

# Create your views here.
def repo(request):
    code_repo_obj = CodeRepo.objects.all()
    return render(request,'repo/repo.html',locals())

def addrepo(request):
    #获取已配置类型为 git 的列表
    sys_list = SystemConfig.objects.filter(sys_type='git')
    if request.method == 'POST':
        add_description = request.POST['repo_description']
        add_name = request.POST['repo_name']
        add_group = request.POST['repo_group']
        add_system = request.POST['repo_system']
        if CodeRepo.objects.filter(repo_system=add_system).filter(repo_name=add_name).filter(repo_group=add_group):
            message = "当前系统已存在你想要创建的 repo"
        else:
            try:
                sys_obj = SystemConfig.objects.get(id=add_system)
                gitlab_obj = Gitlab(sys_obj.sys_api_url,sys_obj.sys_privatetoken)
                print(sys_obj,add_system,gitlab_obj)
                _rel = gitlab_obj.create_project(add_name,add_group,add_description)
                print(_rel)
                if _rel[0]:
                    print(add_name,add_group,add_description,add_system,_rel[2],_rel[3])
                    CodeRepo.objects.create(repo_name=add_name,repo_group=add_group,repo_description=add_description,repo_system=add_system,repo_id=_rel[2],repo_url=_rel[3])
                    return redirect('/repoM/repo')
                else:
                    print(add_name,add_group)
                    message = _rel[1]
            except:
                message = "找不到所选的系统 Id"
    return render(request,'repo/addrepo.html',locals())

def searchrepo(request):
    if request.method == 'POST':
        code_repo_obj = CodeRepo.objects.filter(repo_name__contains=request.POST["repo_search_filter"])
    return render(request,'repo/repo.html',locals())

def importrepo(request):
    sys_list = SystemConfig.objects.filter(sys_type='git')
    if request.method == 'POST':
        message="仓库导入只支持 GitLab 仓库"
        sys_id = request.POST['sys_choice']
        print(sys_id)
        try:
            sys_obj = SystemConfig.objects.get(id=sys_id)
            print("test")
            repo_list = Gitlab(sys_obj.sys_api_url,sys_obj.sys_privatetoken).project_list().projects
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

