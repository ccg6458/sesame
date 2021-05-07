from utils.view import BaseViewSet
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Playbook, Job


# Create your views here.

class PlaybookViewSet(BaseViewSet):
    model = Playbook
    create_require_params = ['name', 'content']


class JobViewSet(BaseViewSet):
    model = Job
    create_require_params = ['name', 'inventory']
