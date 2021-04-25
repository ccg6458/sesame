from utils.view import BaseViewSet
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from .models import Host


# Create your views here.

class HostViewSet(BaseViewSet):
    model = Host

    @action(detail=False)
    def describe(self, request):
        data = {}
        try:
            args = request.GET
            private_ip = args.get('private_ip')
            instance = Host.objects.get(private_ip=private_ip)
            data = instance.to_dict()
        except ObjectDoesNotExist as e:
            self.code = 5000
            self.message = '资源不存在：{}'.format(e.args)
        except Exception as e:
            self.code = 5000
            self.message = '未知错误：{}'.format(e.args)

        return self.json(self.code, self.message, data)
