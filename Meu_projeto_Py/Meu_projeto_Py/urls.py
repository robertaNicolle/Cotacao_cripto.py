# Meu_projeto_Py/urls.py

from django.contrib import admin
from django.urls import path, include  # Não se esqueça de importar o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cotacoes.urls')),  # Inclui as URLs do app cotacoes
]
