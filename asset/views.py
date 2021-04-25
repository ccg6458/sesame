from utils.view import BaseViewSet
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from .models import Host


# Create your views here.

class HostViewSet(BaseViewSet):

    @action(methods=['post'], detail=False)
    def add(self, request):
        code = 0
        message = self.get_message(code)
        require_params = ['private_ip']
        try:
            data = request.data
            params = data.keys()
            for require_param in require_params:
                if require_param not in params:
                    raise Exception('参数缺失：{}'.format(require_param))
            instance = Host(**data)
            instance.save()
        except Exception as e:
            code = 5000
            message = '主机创建失败：{}'.format(e.args)

        return self.json(code, message)

    @action(detail=False)
    def describe(self, request):
        code = 0
        message = self.get_message(code)
        data = []
        try:
            args = request.GET
            private_ip = args.get('private_ip')
            instance = Host.objects.get(private_ip=private_ip)
            data = instance.to_dict()
        except ObjectDoesNotExist as e:
            code = 5000
            message = '资源不存在：{}'.format(e.args)
        except Exception as e:
            code = 5000
            message = '未知错误：{}'.format(e.args)

        return self.json(code, message, data)
