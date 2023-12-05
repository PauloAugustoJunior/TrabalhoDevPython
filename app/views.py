from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import PrevisaoTempoSimples
from django.utils import timezone
from datetime import datetime, timedelta

class home(View):
    def get(self, request):
        datas_futuras = [datetime.now().date() + timedelta(days=i) for i in range(5)]
        objetos = PrevisaoTempoSimples.objects.filter(cidade='São Paulo')
        campos_exibir = ['cidade','uf','dia','resumo','temp_max','temp_min','dir_vento','int_vento','dia_semana','umidade_max','umidade_min']
        dados_exibir = [{campo: getattr(objeto,campo)for campo in campos_exibir}for objeto in objetos]
        dados_exibir = [
            {
                campo: getattr(objeto, campo) if campo != 'dia_semana' else getattr(objeto, campo).split('-')[0]
                for campo in campos_exibir
            }
            for objeto in objetos
        ]
        return render(request,'base.html',{'dados_exibir':dados_exibir})
    
    
# class resultadosPesquisa(View):
#     def get(self, request):
#         objetos = PrevisaoTempoSimples.objects.all()
#         campos_exibir = ['cidade','dia','resumo','temp_max','temp_min','dir_vento','int_vento','dia_semana','umidade_max','umidade_min']
#         dados_exibir = [{campo: getattr(objeto,campo)for campo in campos_exibir}for objeto in objetos]
#         return render(request,'resultados_pesquisa.html',{'resultados': resultados_filtrados}) 

class login(View):
    def get(self, request):
        return render(request,'login.html')
    
  
class cadastrar(View):
    def get(self, request):
        return render(request,'cadastrar.html')
    
class usuario(View):
    def get(self, request):
        return render(request,'usuario.html')    