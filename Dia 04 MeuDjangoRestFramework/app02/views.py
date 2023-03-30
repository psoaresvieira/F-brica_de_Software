from django.shortcuts import render
from rest_framework import viewsets
from app02.serializer import MercadoJogosSerializer
from app02.models import MercadoJogos

# Create your views here.
class MercadoJogosViewSet(viewsets.ModelViewSet):
    queryset = MercadoJogos.objects.all()
    serializer_class = MercadoJogosSerializer