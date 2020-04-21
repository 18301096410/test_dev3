from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import FileResponse
from django.template import RequestContext
from django.http import HttpResponse,StreamingHttpResponse
from django.urls import reverse
from django.utils.http import urlquote
from django.conf import settings
# Create your views here.

from app_big_case.models import File
from app_big_case.forms import UploadForm

from app_big_case.tools import upload_file

import os,shutil,paramiko,datetime



#上传接口
# def upload(request):
#     # if request.method == 'GET':
#     #     return render(request,"big_case/upload.html")
#     if request.method == 'POST':
#         form = UploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             files = request.FILES.getlist('file')
#             for f in files:
#                 file_info = FileInfo(file_name=f.name, file_size=1 if 0 < f.size < 1024 else f.size / 1024,
#                                      file_path=os.path.join('/Users/wangsijia/Desktop/file/upload', f.name))
#                 file_info.save()
#                 destination = open(os.path.join("/Users/wangsijia/Desktop/file/upload", f.name), 'wb+')
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#                     destination.close()
#             # 返回上传页
#             return HttpResponseRedirect('/uploader/list')
#     else:
#         form = UploadForm()
#         return render(request, 'big_case/upload.html', {'form': form})

# 文件列表
def list(request):
    file_infos = File.objects.all()
    return render(request, 'big_case/list.html', {'file_infos': file_infos})



#上传文件
def upload(request):
    if request.method == "POST":       #请求方法为post时，进行处理
        #获取文件名称
        myFile = request.FILES.get("myfile",None)   #如果文件上传为空，则默认显示为None
        print(myFile)
        if not myFile:
            return HttpResponse("没有文件可以上传")
        # 上传到本地文件夹
        # destination = open(os.path.join("/Users/wangsijia/Desktop/file/file_list",myFile.name),'wb+')   #打开文件特定文件的二进制写操作
        # print(destination)
        # # # print(type(myFile))
        # print(myFile.chunks())
        # for chunk in myFile.chunks():   #分块写入文件
        #     print('----------------------')
        #     # print(chunk)
        #     destination.write(chunk)
        #     destination.close()
        #上传文件到服务器
        # print('文件明称是%s' % myFile.name)
        # print('文件的类型是%s' % type(myFile.name))
        local_file = r'/Users/wangsijia/Desktop/file/file_list/' + myFile.name
        remote_path = os.path.join('/home/file/', myFile.name)
        print(remote_path)
        upload_file(local_file, remote_path)
        # print(myFile)

        # return HttpResponse("上传成功")
        return render(request,"big_case/list.html")

    else:
        file_list = []
        files = "/Users/wangsijia/Desktop/file/file_list"
        for i in file_list:
            file_list.append(i)
        return render(request,"big_case/upload.html",{'file_list':file_list})

#下载文件
def download(request):
    filename = request.Get.get('file')
    filepath = os.path.join(settings.MEDIA_ROOT,filename)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)
    # response = FileResponse(fp)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % filename
    return response
    fp.close()






