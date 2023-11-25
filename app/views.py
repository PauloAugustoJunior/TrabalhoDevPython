# import logging

# from django.conf import settings
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import PrevisaoTempoSimples
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# logger = logging.getLogger('sistema2')
# Create your views here.

class home(View):
    def get(self, request):
        objetos = PrevisaoTempoSimples.objects.all()
        return render(request, 'base.html', {'objetos': objetos})
        # return render(request,'base.html')
    
class login(View):
    def get(self, request):
        return render(request,'login.html')
    
  
class cadastrar(View):
    def get(self, request):
        return render(request,'cadastrar.html')
    
class usuario(View):
    def get(self, request):
        return render(request,'usuario.html')    