from django.db import models

# Create your models here.
class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=100, null=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态", default=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    """
    模块表
    """
    #CASCADE为默认级联删除
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  #这个外键和上面的项目是有关联关系的
    name = models.CharField("名称", max_length=100, null=False, default="")
    describe = models.TextField("描述", default="")
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name