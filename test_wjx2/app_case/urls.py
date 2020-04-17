from django.urls import path
from app_case import views

urlpatterns = [

    #默认跳转的路径为case列表
    path("", views.list_case),

]