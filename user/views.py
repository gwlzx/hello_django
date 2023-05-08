from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from one.models import People
from django.http import HttpResponse
from user.utils import *
from one.models import *


def tmp(request):
    return render(request, 'user/home.html')


# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        print(username, passwd)
        passwd = gen_passwd(passwd)
        res = People.objects.filter(name=username, passwd=passwd)
        if not res:
            return HttpResponse("用户或密码错误")
        request.session["username"]  = username
        return HttpResponse("登录成功，欢迎来到%s用户中心"%username)
    return render(request, 'user/index.html')


def reg(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    passwd = request.POST.get("passwd")
    passwd_confirm = request.POST.get("passwd_confirm")
    print(username, email, passwd, passwd_confirm)
    if passwd==passwd_confirm:
        passwd = gen_passwd(passwd)
        People.objects.create(name=username, email=email, passwd=passwd)
        return redirect(reverse(login))
    return HttpResponse("两次填写的密码不一致")