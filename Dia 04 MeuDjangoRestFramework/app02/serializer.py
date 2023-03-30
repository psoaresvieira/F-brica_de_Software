from rest_framework import serializers
from app02.models import MercadoJogos

class MercadoJogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MercadoJogos
        fields = ['id', 'cliente', 'jogo', 'verificar']

