from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from liga.serializer import ChampionsLeagueSerializer
from liga.models import ChampionsLeague
from liga.serializer import TimeSerializer
from liga.models import Time
from liga.serializer import JogadorSerializer
from liga.models import Jogador

# Create your views here.
class ChampionsLeagueViewSet(viewsets.ModelViewSet):
    queryset = ChampionsLeague.objects.all()
    serializer_class = ChampionsLeagueSerializer

class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer