from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm,ProjectEditForm
from django.http import HttpResponseRedirect
from app_manage.models import Module
from app_manage.forms import ModuleForm


def list_module(request):
    '''项目管理'''
    module_list = Module.objects.all
    return render(request, "module/list.html", {
        "modules": module_list})


def add_module(request):
    #判断请求方法是否是post
    if request.method == "POST":
        #如果是post的话，就去请求这个表单
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']  #项目
            name = form.cleaned_data['name']    #名称
            describe = form.cleaned_data['describe']     # 描述
            Module.objects.create(name=name,describe=describe,project=project)   #进行创建数据
        #创建完成之后跳转到模块列表页
        return HttpResponseRedirect("/manage/module_list/")
    else:
        #如果是空的话跳转到project_add界面
        form = ModuleForm()
        #把表单作为一个对象传给到前端
    return render(request, "module/add.html", {"form":form})


def edit_module(request,mid):
    #编辑项目
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():  # 判断里面的值
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']

            m = Module.objects.get(id=mid)
            m.project = project
            m.name = name  # 将下面每一个字段的值进行赋值
            m.describe = describe
            m.save()  # 进行保存
        return HttpResponseRedirect("/manage/module_list/")  # 保存之后的跳转，回到项目列表当中
    else:
        if mid:
            # 先进行查询数据给到表单
            project = Module.objects.get(id=mid)
            form = ProjectEditForm(instance=project)
        else:
            # 否则就是没有pid，form就是返回一个不带数据的表格
            form = ProjectForm()
            # 否则就把它返回
        return render(request, "module/edit.html", {
            "form": form,
            "id": mid
        })

#删除的视图,把这个pid传过来
def delete_module(request,mid):
    """删除项目"""
    if request.method == "GET":
        m = Module.objects.get(id=mid)
        m.delete()
        return HttpResponseRedirect("/manage/module/")
    else:
        return HttpResponseRedirect("/manage/module/")