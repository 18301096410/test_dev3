from django.db import models
from django.utils import timezone

# Create your models here.
class File (models.Model):
    file_name = models.CharField(max_length=500)
    file_size = models.DecimalField(max_digits=10, decimal_places=0)
    file_path = models.CharField(max_length=500)
    upload_time = models.DateTimeField(default=timezone.now())

    #返回文件名称
    def __str__(self):
        return self.file_name