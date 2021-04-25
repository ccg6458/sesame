from utils.view import BaseViewSet
from rest_framework.decorators import action
from .models import Host


# Create your views here.

class HostViewSet(BaseViewSet):
    @action(methods=['post'], detail=False)
    def add(self, request):
        code = 0
        message = self.get_message(code)
        try:
            data = request.data
            instance = Host(**data)
            instance.save()
        except Exception as e:
            code = 5000
            message = '主机创建失败：{}'.format(e.args)

        return self.json(code, message)
