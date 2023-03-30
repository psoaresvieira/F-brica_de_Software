from django.db import models

# Create your models here.
class MercadoJogos (models.Model):
    cliente = models.CharField(max_length=100)
    jogo = models.CharField(max_length=30)
    verificar = models.BooleanField(default=False)
