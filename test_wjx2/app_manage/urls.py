from django.urls import path
# from django.conf.t import url
from django.conf.urls import url
# from views import views
from app_manage.views import project_views,module_views

urlpatterns = [
    # 项目管理     url这个一直有问题，现在用url这种方法暂时解决
    # path("", project_views.manage),
    #默认跳转的路径为项目列表
    path("", project_views.list_project),
    #项目列表
    path('project_list/',project_views.list_project),
    url(r'^project_add', project_views.add_project),
    path('project_edit/<int:pid>/', project_views.edit_project),     #编辑的url
    path('project_delete/<int:pid>/', project_views.delete_project),  # 删除的url

    #模块管理
    path('module_list/',module_views.list_module),
    path('module_add/', module_views.add_module),
    path('module/edit/<int:mid>/',module_views.edit_module),   #这个后面需要一个二级的目录
    path('module_delete/<int:mid>/', module_views.delete_module),  # 删除的url

]