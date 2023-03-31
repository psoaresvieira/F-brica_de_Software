from rest_framework import serializers
from app23.models import ChampionsLeague
from app23.models import Time
from app23.models import Jogador


class ChampionsLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionsLeague
        fields = ['id', 'time']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'tnome', 'estadio']

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ['id', 'jnome', 'posicao']
