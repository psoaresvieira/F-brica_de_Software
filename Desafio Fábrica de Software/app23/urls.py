from rest_framework import routers
from app23.views import ChampionsLeagueViewSet
from app23.views import TimeViewSet
from app23.views import JogadorViewSet

router = routers.DefaultRouter()
router.register(r'', ChampionsLeagueViewSet)

router = routers.DefaultRouter()
router.register(r'', TimeViewSet)

router = routers.DefaultRouter()
router.register(r'', JogadorViewSet)

urlpatterns = router.urls