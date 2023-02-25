from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class TestTemplateView(TemplateView):
    # 设置模板文件
    template_name = "test_templateview.html"
    # 重写父类的get_content_data()方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context["info"] = "该变量可以传递到模板"
        return context

class TestListView(ListView):
    model = UserBaseInfo
    template_name = "test_listview.html"
    # 设置模板变量的上下文
    context_object_name = "users"
    # 每页显示的条数
    paginate_by = 1
    # 重写父类的get_queryset()方法
    def get_queryset(self):
        # 返回状态为1的数据
        userinfo = UserBaseInfo.objects.filter(status=1)
        return userinfo
    # 重写父类的get_context_data()方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context["info"] = "ListView 变量可以传递到模板"
        print(context)
        return context


class TestDetalView(DetailView):
    model = UserBaseInfo
    template_name = "test_detailview.html"
    # 设置模板变量
    context_object_name = "users"
    # 对应路由中的参数userid
    pk_url_kwarg = 'userid'
    
