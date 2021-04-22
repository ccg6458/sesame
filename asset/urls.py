from django.urls import path

from .views import TestView
urlpatterns = [
    path(r'<str:action>', TestView.as_view()),

]