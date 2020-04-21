from django.shortcuts import render
from django.http import JsonResponse    #这个就是返回一个json格式的数据
from django.core.paginator import Paginator,PageNotAnInteger

from app_manage.models import Project,Module
from app_case.models import TestCase

import requests,json

# Create your views here.

def list_case(request):
    '''用例列表'''
    cases = TestCase.objects.all()
    #获取所有的数据，一页按照几条分
    p = Paginator(cases,2)
    #去获取这个页数信息
    page = request.GET.get("page","")
    if page == "":
        page = 1
    try:
        #把这个页数给到前端
        page_case = p.page(page)
    except PageNotAnInteger:
        #如果不是一个整型的时候，取第一页
        page_case = p.page(1)
    except:
        #如果超出页数就给出最后一页的
        page_case = p.page(p.num_pages)
    #查出表中所有的数据，作为一个字段进行返回，这里面是分页之后的数据
    return render(request,"case/list.html",{
        "cases":page_case
    })

def send_req(request):
    if request.method == "GET":
        url = request.GET.get("url","")
        method = request.GET.get("method","")
        header = request.GET.get("header","")
        per_type = request.GET.get("par_type","")
        per_value = request.GET.get("per_value"," ")

        # 校验url
        if url=="":
            return JsonResponse({"status": 10101,
                                 "message": "url不能为空"})
        #转换hesder跟值
        header = json.loads(header)
        try:
            per_value = json.loads(per_value)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"status": 10102,
                                 "message": "Header格式错误"})
        # try:
        #     per_value = json.loads(per_value)
        # except json.decoder.JSONDecodeError:
        #     return JsonResponse({"status": 10103,
        #                          "message": "参数格式错误，必须是标准json格式"})

        # per_value = json.loads(per_value)
        if method == 'get':
            r = requests.get(url,params=per_value,headers=header)


        if method == "post":
            if per_type == "form":
                r = requests.post(url,data=per_value,headers=header)
            if per_type == "json":
                r = requests.post(url,json=per_value,headers=header)
            # else:
            #     return JsonResponse({"status": 10101,
            #                          "message": "参数类型错误",})

            return JsonResponse({"code":10200,
                             "message":"success","data":r.text})


def assert_result(request):
    '''断言结果'''
    if request.method == "POST":
        #返回结果
        result_text = request.POST.get("result_text","")
        # 校验结果
        assert_text = request.POST.get("assert_text","")
        #包含
        assert_type = request.POST.get("assert_type","")
        if result_text == "" or assert_text == "":
            return JsonResponse({"code":10101,"message":"断言的参数不能为空"})
        if assert_type != "include" and assert_type !="equal":
            return JsonResponse({"code":10101,"message":"断言的参数不能为空"})
        if assert_type == "include":
            if assert_text in result_text:
                return JsonResponse({"code": 10200, "message": "断言包含成功"})
            else:
                return JsonResponse({"code": 10200, "message": "断言包含失败"})
        if assert_type == "equal":
            if assert_text == result_text:
                return JsonResponse({"code": 10200, "message": "断言相等成功"})
            else:
                return JsonResponse({"code": 10200, "message": "断言相等失败"})
        return JsonResponse({"code": 10102, "message": "fail"})


def get_select_data(request):
    if request.method == "GET":        #获取select下拉框需要的项目/模块数据
        projects = Project.objects.all()            #获取所有的项目数据
        print("project的类型%s" % type(projects))
        data_list = []
        for p in projects:          #循环表内的数据
            project_dict = {
                "id":p.id,
                "name":p.name
            }
            modules = Module.objects.filter(project=p)
            print("module的类型%s"%type(modules))
            module_list = []
            for m in modules:
                module_dict = {
                    "id": m.id,
                    "name": m.name}
                module_list.append(module_dict)                   #追加项目下面相关的所有的模块
            # print()
            project_dict["moduleList"] = module_list    #把模块追加到项目下面
            data_list.append(project_dict)              #获取项目之后添加到list当中
        return JsonResponse({"code":10200,"message":"success","data":data_list})


def save_case(request):
    '''保存用例'''
    if request.method == "POST":
        case_id = request.POST.get("cid", "")
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        per_type = request.POST.get("per_type", "")
        per_value = request.POST.get("per_value", "")
        result_text = request.POST.get("result_text", "")
        variable = request.POST.get("variable", "")
        assert_text = request.POST.get("assert_text", "")   #断言的文本
        assert_type = request.POST.get("assert_type", "")   #断言的类型
        module_id = request.POST.get("module_id", "")
        case_name = request.POST.get("case_name", "")

        if method == 'get':
            method_int = 1
        elif method == 'post':
            method_int = 2
        else:
            return JsonResponse({"code": 10101, "message": "参数类型错误"})

        if per_type == 'form':
            per_type_int = 1
        elif per_type == 'json':
            per_type_int = 2
        else:
            return JsonResponse({"code": 10102, "message": "参数类型错误"})

        if assert_type == "include":
            assert_type_int = 1
        elif assert_type == "equal":
            assert_type_int = 2
        else:
            return JsonResponse({"code": 10103, "message": "参数类型错误"})




        TestCase.objects.create(
            # url=url,
            module_id=module_id,
            name=case_name,
            method=method_int,
            header=header,
            parameter_type= per_type_int,
            parameter_body=per_value,
            result=result_text,
            assert_text=assert_text,
            assert_type=assert_type_int,
        )
        return JsonResponse({"code": 10200, "message": "create success"})

#添加用例的时候返回debug


def add_case(request):
    '''创建用例'''
    return render(request,"case/debug.html")

def edit_case(request):
    '''编辑用例'''
    return render(request,'case/edit.html')




