from django.db import models
from uuid import uuid4
from django.utils import timezone
import os

def date_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()

    return '/'.join([
        'video/'+ymd_path,
        uuid_name + extension,
        ])

class MediaModel(models.Model):
    video = models.FileField(upload_to=date_upload_to, blank=True, null=True)
    original_file_name = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(default=timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
    filesize = models.CharField(max_length=10, null=True)



# Create your models here.
