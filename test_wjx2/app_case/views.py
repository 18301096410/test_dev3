from django.shortcuts import render

# Create your views here.

def list_case(request):
    return render(request,"case/debug.html")

def add_case(request):
    '''创建用例'''
    return render(request,"case/debug.html")

def edit_case(request):
    '''编辑用例'''
    return render(request,'case/edit.html')




