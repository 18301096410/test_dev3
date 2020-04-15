from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm,ProjectEditForm
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def manage(request):
    '''项目管理'''
    projects_list = Project.objects.all
    return render(request, "project_list.html", {"projects":projects_list})

def add_project(request):
    #判断请求方法是否是post
    if request.method == "POST":
        #如果是post的话，就去请求这个表单
        form = ProjectForm(request.POST)
        if form.is_valid():
            #名称
            name = form.cleaned_data['name']
            # 描述
            describe = form.cleaned_data['describe']
            # 状态
            status = form.cleaned_data['status']
            #进行创建数据
            Project.objects.create(name=name,describe=describe,status=status)
        #创建完成之后跳转到项目界面
        return HttpResponseRedirect("/project/")
    else:
        #如果是空的话跳转到project_add界面
        form = ProjectForm()
        #把表单作为一个对象传给到前端
    return render(request, "project_add.html", {"form":form})

#编辑项目，这个pid就是连接中的id
def edit_project(request,pid):
    # if request.method == "POST":
    #     #更新
    #     form = ProjectForm(request.POST)
    #     if form.is_valid():     #判断里面的值
    #         name = form.cleaned_data['name']    # 名称
    #         describe = form.cleaned_data['describe']    # 描述
    #         status = form.cleaned_data['status']    # 状态
    #         p = Project.objects.get(id=pid)
    #         p.name = name   #将下面每一个字段的值进行赋值
    #         p.describe = describe
    #         p.status = status
    #         p.save()    #进行保存
    #     return HttpResponseRedirect("/manage/")     #保存之后的跳转，回到项目列表当中
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/manage/")
    else:
        if pid:
            #先进行查询数据给到表单
            project = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=project)
        else:
            #否则就是没有pid，form就是返回一个不带数据的表格
            form = ProjectForm()
            #否则就把它返回
        return render(request,"project_edit.html",{
            "form":form,
            "id":pid
        })

#删除的视图,把这个pid传过来
def delete_project(request,pid):
    if request.method == "GET":
        p = Project.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")






