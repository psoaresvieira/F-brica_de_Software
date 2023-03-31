from django.shortcuts import render
from rest_framework import viewsets
from app23.serializer import ChampionsLeagueSerializer
from app23.models import ChampionsLeague
from app23.serializer import TimeSerializer
from app23.models import Time
from app23.serializer import JogadorSerializer
from app23.models import Jogador

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

