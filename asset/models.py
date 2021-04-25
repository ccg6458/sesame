from django.db import models


# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=64, verbose_name='主机名', null=True)
    private_ip = models.CharField(max_length=16, verbose_name='内网ip')
    public_ip = models.CharField(max_length=16, verbose_name='内网ip', null=True)
    cpu = models.CharField(max_length=64, verbose_name='cpu', null=True)
    memory = models.CharField(max_length=64, verbose_name='memory', null=True)
    disk = models.CharField(max_length=256, verbose_name='disk', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
