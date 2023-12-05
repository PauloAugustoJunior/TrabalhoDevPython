from django.contrib import admin
from django.urls import path
from app.views import home, login, cadastrar,usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(), name = 'home'),
    path('login/',login.as_view(), name = 'login'),
    path('cadastrar/',cadastrar.as_view(), name = 'cadastrar'),
    path('usuario/',usuario.as_view(), name = 'usuario'),
]
