from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.core.exceptions import ObjectDoesNotExist
from .http_code import Code
import datetime


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    关闭csrf验证
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class BaseResponse:

    @staticmethod
    def json(code=0, message=None, data=None, **kwargs):
        """

        :param code: 返回状态码
        :param message: 返回信息
        :param data: 返回数据
        :param kwargs: 其他参数
        :return: 封装Response
        """
        if data is None:
            data = []
        if message is None:
            message = Code.code_msg.get(code, Code.code_unknow_msg)
        ret = {
            'code': code,
            'message': message,
            'data': data
        }
        response = Response(ret, **kwargs)
        return response


class CURDMixin:
    model = None
    code = Code.Ok
    message = Code.default_msg
    create_require_params = []  # 执行create方法时的必备参数列表，无则为空

    def create(self, request):
        model = self.model
        model_name = self.model._meta.model_name
        try:
            data = request.data
            params = data.keys()
            for require_param in self.create_require_params:
                if require_param not in params:
                    raise Exception('参数缺失：{}'.format(require_param))
            instance = model(**data)
            instance.save()
            self.message = '{}创建成功'.format(model_name)

        except Exception as e:
            self.code = 5000
            self.message = '{}创建失败：{}'.format(model_name, e.args)

        return BaseResponse.json(self.code, self.message)

    def list(self, request):
        model = self.model
        data = []
        try:
            query_set = model.objects.all()
            for query in query_set:
                data.append(query.to_dict())
        except Exception as e:
            self.code = 5000
            self.message = '未知错误：{}'.format(e.args)

        return BaseResponse.json(self.code, self.message, data=data)

    def retrieve(self, request, pk):
        model = self.model
        data = []
        try:
            query = model.objects.get(id=pk)
            data = query.to_dict()
        except ObjectDoesNotExist as e:
            self.code = 5000
            self.message = '资源不存在：{}'.format(e.args)
        except Exception as e:
            self.code = 5000
            self.message = '未知错误：{}'.format(e.args)

        return BaseResponse.json(self.code, self.message, data)

    def update(self, request, pk):
        model = self.model
        model_name = self.model._meta.verbose_name
        try:
            data = request.data
            obj = model.objects.get(id=pk)
            data['modify_time'] = datetime.datetime.now()
            obj.__dict__.update(**data)
            obj.save()
            self.message = '{}修改成功'.format(model_name)
        except ObjectDoesNotExist as e:
            self.code = 5000
            self.message = '资源不存在：{}'.format(e.args)
        except Exception as e:
            self.code = 5000
            self.message = '未知错误：{}'.format(e.args)

        return BaseResponse.json(self.code, self.message)


class BaseViewSet(ViewSet, BaseResponse, CURDMixin):
    """
    重写ViewSet，添加自定义response方法
    """
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)
