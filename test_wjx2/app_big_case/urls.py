from django.urls import path
# from django.conf.t import url
from django.conf.urls import url
# from app_manage.views import project_views,module_views
from app_big_case import views


urlpatterns = [
    path('',views.list),  # 列表
    path('upload/',views.upload),  # 上传
    path('download/<id>/',views.upload),

]