from django.shortcuts import render
from util.view import BaseView


# Create your views here.

class TestView(BaseView):
    get_actions = ['test']

    def test(self, request):
        return self.json()
