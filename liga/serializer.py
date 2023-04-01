from rest_framework import serializers
from liga.models import ChampionsLeague
from liga.models import Time
from liga.models import Jogador

class ChampionsLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionsLeague
        fields = ['id', 'temporada']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'nome', 'estadio', 'temporada']

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ['id', 'nome', 'posicao', 'time']