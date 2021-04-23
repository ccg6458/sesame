from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TestViewSet

router = SimpleRouter()
router.register(r'test', TestViewSet, 'test')
urlpatterns = router.urls
