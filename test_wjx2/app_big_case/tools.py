import paramiko,os,datetime

hostname = '123.56.99.22'
username = 'root'
password = 'Sj123456'
port = 22  # 配置信息可以写到配置文件中
def upload_file(local_file, remote_path):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print('开始上传文件%s ' % datetime.datetime.now())

        try:
            # print('文件明称是%s' % myFile.name)
            # print('文件的类型是%s' % type(myFile.name))
            sftp.put(local_file, remote_path)
        except Exception as e:
            #创建文件夹
            # sftp.mkdir(os.path.split(remote_path)[0])
            sftp.put(local_file, remote_path)
            print("从本地： %s 上传到： %s" % (local_file, remote_path))
        print('文件上传成功 %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(repr(e))
if __name__ == "__main__":
    local_file = r'/Users/wangsijia/Desktop/file/file_list/test1.py'
    file_name = local_file.split('/')[-1]
    remote_path = os.path.join('/home/file/',file_name)
    upload_file(local_file, remote_path)
    # print(os.path.split(remote_path)[0])
    # print(a)