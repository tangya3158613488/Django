from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse("app2中的index方法")

def show(request, id):
    return HttpResponse("app2中的show方法，参数为id，值为"+str(id))

def show_uuid(request, id):
    return HttpResponse("app2中的show_uuid方法，参数为id，值为"+str(id))

def show_slug(request, q):
    return HttpResponse("app2中的show_slug方法，参数为q，值为"+str(q))

def article_list(request, year):
    return HttpResponse("app2中的article_list方法，参数为year，指定4位，值为"+str(year))

def article_page(request, page, key):
    return HttpResponse("app2中的article_page方法，参数为page，任意数字，值为"+str(page)+" 参数key，字母数字下划线，值为"+str(key))

def url_reverse(request):
    # 使用reverse()方法反向解析
    print("在views()函数中使用reverse()方法解析的结果："+reverse("app2_url_reverse"))
    return render(request, "url_reverse.html")