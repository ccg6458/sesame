from utils.view import BaseViewSet
from rest_framework.decorators import action


# Create your views here.

class TestViewSet(BaseViewSet):

    @action(methods=['get', 'post', 'put'], detail=False)
    def aaa(self, request):
        return self.json()

    @action(methods=['get', 'post', 'put'], detail=False, permission_classes=[])
    def bbb(self, request):
        return self.json()
