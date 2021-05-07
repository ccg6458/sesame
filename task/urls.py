from rest_framework.routers import SimpleRouter
from .views import PlaybookViewSet, JobViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'pb', PlaybookViewSet, 'playbook')
router.register(r'job', JobViewSet, 'job')
urlpatterns = router.urls
