from rest_framework import routers
from app02.views import MercadoJogosViewSet

router = routers.DefaultRouter()
router.register(r'', MercadoJogosViewSet)

urlpatterns = router.urls