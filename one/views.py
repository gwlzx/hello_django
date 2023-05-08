import json

import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator

from one.models import *
from blog.models import Post
import markdown
from markdown.extensions.toc import TocExtension

def get_page(request, page_num):
    post_list = People.objects.all()
    paginator = Paginator(post_list, 3)
    page = paginator.page(page_num)
    page_list = page.object_list
    page_range = paginator.page_range
    context = {"page_list": page_list, "page_range": page_range, "page":page}
    return render(request, "one/paginator.html", context=context)


# Create your views here.
def add_people(request):
    if request.method=="GET":
        return render(request, 'one/add_people.html')
    elif request.method=="POST":
        username = request.POST.get("username")
        age = request.POST.get("age")
        p1 = People.objects.create(name=username, age=age)
        return redirect(reverse("contact:people_detail", kwargs={"pk":p1.id} ))


def people_list(request):
    p_list = Post.objects.all()
    print(type(p_list))
    print(p_list)
    return render(request, "one/people_list.html", context={"p_list": p_list})


def people_detail(request, pk):
    p = Post.objects.get(id=pk)
    p.body = markdown.markdown(p.body,
                         extensions=[
                             'markdown.extensions.extra',
                             'markdown.extensions.codehilite',
                             'markdown.extensions.toc',
                         ])
    return render(request, "one/people_detail.html", context={"p":p})


def delete_people(request, id):
    p = get_object_or_404(People, id=id)
    p.delete()
    return HttpResponseRedirect("/contact/peoples")


def index(request):
    resp = HttpResponse(content_type="application/json")
    resp.write("Hello World!")
    resp.status_code = 404
    resp.charset = "UTF8"
    return resp


def get_data(request):
    # 从热门微博的接口中采集数据
    # resp = requests.get("https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0")
    # 将热门微博数据转换成Python对象（字典，列表）
    # data = resp.json()
    # 将Python对象转换为json字符串
    user_info = {"name":"Alice", "age":18}
    # 返回json字符串并指定content_type为json格式
    return JsonResponse(user_info)


def home(request):
    username = request.session.get("user")
    from django.template import loader
    print("请求的路由为：", request.path)
    print("请求的编码为：", request.encoding)
    print("请求的方法为：", request.method)
    print("GET请求参数为：", request.GET.keys())
    print("POST请求参数为：", request.POST.keys())
    print("请求中COOKIES为：", request.COOKIES.keys())
    print("请求中session为：", request.session.keys())
    wd = request.GET.getlist("wd")
    print(wd)
    js = "<script>alert('你的电脑中毒了！....')</script>"
    html = "<h1 style='color:red'>这是一级标题</h1>"
    content = loader.render_to_string('one/home.html', context={'user':username, 'js':js, 'html':html})
    return HttpResponse(content)
    # return render(request, 'one/home.html')


def save_pic(request):
    from hello_django.settings import BASE_DIR
    import datetime
    import os
    import random
    datetime_str = datetime.datetime.now().strftime("-%Y%m%d%H%M%S-")+str(random.randrange(1000))
    file = request.FILES.get("pic")
    file_name = file.name.split(".")[0]+datetime_str+".png"
    p = os.path.join(BASE_DIR, 'static', 'img', 'test', file_name)
    with open(p, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return HttpResponse("上传成功！")


from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO


# verify_code
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype()
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')