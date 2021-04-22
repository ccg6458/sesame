from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from .http_code import Code


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    关闭csrf验证
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class BaseView(APIView):
    """
    重写APIVIEW，利用反射机制访问到不同View内的方法
    """
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)
    get_actions = []
    post_actions = []
    put_actions = []

    def action(self, request, action, actions):
        if action in actions:
            func = getattr(self, action)
            return func(request)
        return self.json(code=5000, message=str(action) + '方法不存在')

    def get(self, request, action=None):
        """
        APIView get方法重写
        :param request: django request对象
        :param action: url所带的action参数，对应View内的action方法
        :return:
        """
        actions = self.get_actions
        return self.action(request, action, actions)

    def post(self, request, action=None):
        """
        APIView post方法重写
        :param request:
        :param action:
        :return:
        """
        actions = self.post_actions
        return self.action(request, action, actions)

    def put(self, request, action=None):
        """
        APIView put方法重写
        :param request:
        :param action:
        :return:
        """
        actions = self.put_actions
        return self.action(request, action, actions)

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
