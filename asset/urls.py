from rest_framework.routers import SimpleRouter
from .views import HostViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'host', HostViewSet, 'host')
urlpatterns = router.urls
