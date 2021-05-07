from django.db import models
from utils.model import ModelMixin
from user.models import User
from time import time


# Create your models here.
class Playbook(models.Model, ModelMixin):
    name = models.CharField(max_length=64, verbose_name='剧本名称')
    content = models.TextField(verbose_name='剧本内容')
    version = models.CharField(max_length=64, verbose_name='版本号', default='')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.version:
            self.version = 'v_{}'.format(time())
        self.id = None
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}_{}'.format(self.name, self.version)


class Job(models.Model, ModelMixin):
    name = models.CharField(max_length=64, verbose_name='任务名称')
    inventory = models.CharField(max_length=256, verbose_name='主机清单')
    pb = models.ForeignKey(Playbook, on_delete=models.DO_NOTHING, related_name='job', db_constraint=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='job', db_constraint=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
