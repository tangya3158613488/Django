from django.shortcuts import render
from django.http import HttpResponse

# 定义视图函数，将渲染结果输出到index.html模板中
def index(request):
    return render(request, 'index.html')
