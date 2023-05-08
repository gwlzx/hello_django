from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from one.models import People


# Create your views here.
def register(request):
    return render(request, "register/register.html")


def login(request):
    return render(request, 'register/login.html')


def val_user(request):
    username = request.POST.get("username")
    age = request.POST.get("age")
    user = People.objects.filter(name=username, age=age)
    print(user.query)
    if user:
        request.session["user"] = username
        request.session.set_expiry(60)
        resp = redirect("/")
        # resp.set_cookie("username", username, 60)
        return resp
    resp = redirect("/")
    return resp



def logout(request):
    request.session.clear()
    resp = redirect("/")
    return resp


