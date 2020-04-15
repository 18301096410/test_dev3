from django.urls import path
# from django.conf.t import url
from django.conf.urls import url
from app_manage import views

urlpatterns = [
    # 项目管理     url这个一直有问题，现在用url这种方法暂时解决
    path("", views.manage),
    url(r'^add', views.add_project),
    path('edit/<int:pid>/', views.edit_project),     #编辑的url
    path('delete/<int:pid>/', views.delete_project)  # 编辑的url

]