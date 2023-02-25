from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from app2.models import UserBaseInfo


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

def test_get(request):
    print(request.get_host())
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.GET)
    print(request.META ["HTTP_USER_AGENT"])
    print(request.META["REMOTE_ADDR"])
    print(request.GET.get('username'))
    return HttpResponse("")

def test_post(request):
    print(request.method)
    print(request.POST.get('username'))
    return render(request, 'test_post.html')

def test_response(request):
    response = HttpResponse()
    response.write("hello django")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return response

def test_render(request):
    return render(request, test_render.html, {'info': 'hello django'}, content_type='text/html')

def test_redirect_model(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)

def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号："+str(user.id)+"姓名："+user.username)

def test_redirect_views(request, id):
    return redirect('app2_userinfo', id)

def test_redirect(request):
    return redirect("https://www.baidu.com")
