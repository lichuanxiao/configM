from django.shortcuts import render,redirect
from .models import ProjectList
# Create your views here.

def createproject(request):
    pass

def project(request):
    projects = ProjectList.objects.all()
    return render(request,'project/project.html',locals())

def addproject(request):
    if request.method == 'POST':
        try:
            ProjectList.objects.get(project_key=request.POST["project_key"])
            message = "项目键值不能重复"
            return render(request, 'project/addproject.html',locals())
            # 添加 project_key
        except:
            ProjectList.objects.create(project_name=request.POST['project_name'],project_type=request.POST['project_type'],description=request.POST['project_description'],project_key=request.POST['project_key'].upper())
            return redirect('/projectM/project/')
    return render(request, 'project/addproject.html',locals())