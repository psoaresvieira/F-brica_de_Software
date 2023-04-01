from django.db import models

# Create your models here.
class ChampionsLeague (models.Model):
    temporada = models.CharField(max_length=100)
    def _str_(self):
        return self.temporada
    

class Time (models.Model):
    nome = models.CharField(max_length=100)
    estadio = models.CharField(max_length=40)
    temporada = models.ForeignKey("ChampionsLeague", on_delete=models.CASCADE, related_name="Time")
    def _str_(self):
        return self.temporada.nome

class Jogador (models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=100)
    time = models.ForeignKey("Time", on_delete=models.CASCADE, related_name="Jogador")
    def _str_(self):
        return self.time.nome