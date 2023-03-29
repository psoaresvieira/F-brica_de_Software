from rest_framework import routers
from app01.views import ToDoViewSet

router = routers.DefaultRouter()
router.register(r'', ToDoViewSet)

urlpatterns = router.urls
