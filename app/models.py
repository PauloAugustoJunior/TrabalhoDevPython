from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    locaUsuario = models.CharField(max_length=255)
