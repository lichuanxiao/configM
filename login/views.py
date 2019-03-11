from django.shortcuts import render,HttpResponse,redirect
from .models import User
from .form import UserForm,RegisterForm

# Create your views here.

def get_user(username,pwd):
    try:
        user_obj = User.objects.get(username=username)
    except:
        return (False, "用户不存在")
    if pwd != user_obj.password:
        print("密码不正确")
        return (False, "密码不正确")
    print("succeed!")
    return (True, "验证成功")

def index(request):
    userlist = User.objects.all()
    return render(request, 'index.html', {"userlist":userlist})



def login(request):
    message = None
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user_confirm,message = get_user(username,password)
            if user_confirm:
                request.session['is_login'] = True
                request.session['username'] = username
                return redirect('/index/')
            return render(request,'login.html',locals())
    login_form = UserForm()
    return render(request, 'login.html',locals())

def logout(request):
    request.session.flush()
    return redirect('/login/')


def adduser(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            fullname = register_form.cleaned_data['fullname']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            try:
                user_obj =  User.objects.get(username=username)
                message = "用户已存在"
                return render(request,'adduser.html',locals())
            except:
                if password1 != password2:
                    message = "密码不一致"
                    return render(request,'adduser.html',locals())
                User.objects.create(username=username,fullname=fullname,password=password1,email=email,sex=sex)
                return redirect('/user/')
    register_form = RegisterForm()
    return render(request,'adduser.html', locals())


def user(request):
    userlist = User.objects.all()
    if request.method == 'POST':
        pass
    return render(request,'user.html',locals())


def deleteuser(request,user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/user/')

def edituser(request,user_id):
    userinfo = User.objects.filter(id=user_id).values()[0]
    if request.method == 'POST':
        editinfo = request.POST.dict()
        if editinfo['password1'] != editinfo['password2']:
            message = "密码不一致"
            return render(request,'edituser.html',locals())
        User.objects.filter(id=user_id).update(username=editinfo['username'],fullname=editinfo['fullname'],password=editinfo['password1'],email=editinfo['email'],sex=editinfo['sex'])
        return redirect('/user/') 
    return render(request,'edituser.html',locals())

def searchuser(request):
    if request.method == 'POST':
        user_search = request.POST.dict()['user_search_filter']
        userlist = User.objects.filter(username__icontains=user_search)
        if  not userlist:
           userlist = User.objects.filter(email__icontains=user_search) 
    return render(request,'user.html',locals())   