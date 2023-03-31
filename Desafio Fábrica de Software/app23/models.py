from django.db import models

# Create your models here.
class ChampionsLeague (models.Model):
    time = models.CharField(max_length=100)

class Time (models.Model):
    nome = models.CharField(max_length=100)
    estadio = models.CharField(max_length=40)

class Jogador (models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=100)
