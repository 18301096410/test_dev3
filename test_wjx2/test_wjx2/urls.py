"""test_wjx2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app_person import views
from app_manage.views import module_views
from app_big_case import views as big_views

urlpatterns = [
    path('admin/', admin.site.urls),

# 账户管理
    path('', views.login),
    path('login/',views.login),
    path('logout/',views.logout),
    # 项目/模块管理
#     path('manage/',manage_views.manage),
#     path('project/', include('app_manage.urls')),


    #项目/模块管理
    path('manage/',include('app_manage.urls')),


    #模块管理,这个就是指向到模块管理的url里面
    path('module/', include('app_manage.urls')),

    #用例管理
    path('case/',include('app_case.urls')),

    #上传下载文件接口
    path('big_case/',include('app_big_case.urls')),
    path('big_case/upload/',big_views.upload),

]
