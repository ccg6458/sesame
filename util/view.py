from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .http_code import Code


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    关闭csrf验证
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class BaseViewSet(ViewSet):
    """
    重写ViewSet，添加自定义response方法
    """
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)

    def json(self, code=0, message=None, data=[], **kwargs):
        """

        :param code: 返回状态码
        :param message: 返回信息
        :param data: 返回数据
        :param kwargs: 其他参数
        :return: 封装Response
        """
        if not message:
            message = Code.code_msg.get(code, Code.code_unknow_msg)
        ret = {
            'code': code,
            'message': message,
            'data': data
        }
        response = Response(ret, **kwargs)
        return response
