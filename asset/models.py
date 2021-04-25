from django.db import models


# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=64, verbose_name='主机名', null=True)
    private_ip = models.CharField(max_length=16, verbose_name='内网ip')
    public_ip = models.CharField(max_length=16, verbose_name='内网ip', null=True)
    cpu = models.CharField(max_length=64, verbose_name='cpu', null=True)
    memory = models.CharField(max_length=64, verbose_name='memory', null=True)
    disk = models.CharField(max_length=256, verbose_name='disk', null=True)
    status = models.SmallIntegerField(verbose_name='状态', default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def to_dict(self):
        __exclude_fields = []
        data = {}
        # 序列化逻辑简单，直接获取实例属性即可
        for field in self._meta.fields:
            field_name = field.name
            if field_name not in __exclude_fields:
                data[field_name] = getattr(self, field_name)
        return data
