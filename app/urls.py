# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.views import home,login,cadastrar,usuario

# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',home.as_view(), name = 'home'),
    path('login/',login.as_view(), name = 'login'),
    path('cadastrar/',cadastrar.as_view(), name = 'cadastrar'),
    path('usuario/',usuario.as_view(), name = 'usuario'),
]
