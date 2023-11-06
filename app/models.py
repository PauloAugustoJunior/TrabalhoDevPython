from django.db import models

# Create your models here.

class Usuario(models.model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
