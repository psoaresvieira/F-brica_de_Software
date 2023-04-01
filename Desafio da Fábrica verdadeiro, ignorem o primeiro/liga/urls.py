from liga.views import ChampionsLeagueViewSet, TimeViewSet, JogadorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'championsleague', ChampionsLeagueViewSet, basename='champions')
router.register(r'time', TimeViewSet, basename='times')
router.register(r'jogador', JogadorViewSet, basename='jogadores')

urlpatterns = router.urls

