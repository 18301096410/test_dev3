from django.urls import path
from app_case import views

urlpatterns = [

    #默认跳转的路径为case列表
    path("", views.list_case),
    path('send_req/',views.send_req),
    path('assert_result/',views.assert_result),

    path('get_select_data/',views.get_select_data),


]