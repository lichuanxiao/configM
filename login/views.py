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


def register(request):
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
                return render(request,'register.html',locals())
            except:
                if password1 != password2:
                    message = "密码不一致"
                    return render(request,'register.html',locals())
                User.objects.create(username=username,fullname=fullname,password=password1,email=email,sex=sex)
                return redirect('/index/')
    register_form = RegisterForm()
    return render(request,'register.html', locals())