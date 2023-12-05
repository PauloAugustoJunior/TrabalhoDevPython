from django.db import models

class PrevisaoTempoSimples(models.Model):
    cidade = models.CharField(max_length=255, null=True)
    dia = models.CharField(max_length=255, null=True)
    uf = models.CharField(max_length=255, null=True)
    entidade = models.CharField(max_length=255, null=True)
    resumo = models.CharField(max_length=255, null=True)
    tempo = models.CharField(max_length=255, null=True)
    temp_max = models.IntegerField(default=-1)
    temp_min = models.IntegerField(default=-1)
    dir_vento = models.CharField(max_length=255, null=True)
    int_vento = models.CharField(max_length=255, null=True)
    dia_semana = models.CharField(max_length=255, null=True)
    umidade_max = models.IntegerField(default=-1)
    umidade_min = models.IntegerField(default=-1)
    temp_max_tende = models.CharField(max_length=255, null=True)
    cod_temp_max_tende_icone = models.CharField(max_length=255, null=True)
    temp_min_tende = models.CharField(max_length=255, null=True)
    estacao = models.CharField(max_length=255, null=True)
    hora = models.CharField(max_length=255, null=True)
    nascer = models.CharField(max_length=255, null=True)
    ocaso = models.CharField(max_length=255, null=True)
    fonte = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'previsao_tempo_simples'

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    local_usuario = models.CharField(max_length=100)