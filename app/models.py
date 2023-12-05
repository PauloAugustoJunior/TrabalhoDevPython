from django.db import models

class PrevisaoTempoSimples(models.Model):
    cidade = models.CharField(max_length=255, null=True)
    dia = models.DateField(null=True)
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

class PrevisaoTempoDetalhada(models.Model):
    DC_NOME = models.CharField(max_length=255, null=True, blank=True)
    PRE_INS = models.FloatField(null=True)
    TEM_SEN = models.FloatField(null=True)
    VL_LATITUDE = models.CharField(max_length=50, null=True, blank=True)
    PRE_MAX = models.FloatField(null=True)
    UF = models.CharField(max_length=2, null=True, blank=True)
    RAD_GLO = models.FloatField(null=True)
    PTO_INS = models.FloatField(null=True)
    TEM_MIN = models.FloatField(null=True)
    VL_LONGITUDE = models.CharField(max_length=50, null=True, blank=True)
    UMD_MIN = models.FloatField(null=True)
    PTO_MAX = models.FloatField(null=True)
    VEN_DIR = models.IntegerField(null=True)
    DT_MEDICAO = models.DateField(null=True)
    CHUVA = models.FloatField(null=True)
    PRE_MIN = models.FloatField(null=True)
    UMD_MAX = models.FloatField(null=True)
    VEN_VEL = models.FloatField(null=True)
    PTO_MIN = models.FloatField(null=True)
    TEM_MAX = models.FloatField(null=True)
    TEN_BAT = models.FloatField(null=True)
    VEN_RAJ = models.FloatField(null=True)
    TEM_CPU = models.FloatField(null=True)
    TEM_INS = models.FloatField(null=True)
    UMD_INS = models.FloatField(null=True)
    CD_ESTACAO = models.CharField(max_length=255, null=True, blank=True)
    HR_MEDICAO = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'previsao_tempo_detalhada'

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    local_usuario = models.CharField(max_length=100)