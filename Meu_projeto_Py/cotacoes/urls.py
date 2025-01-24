# cotacoes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cotacao/', views.cotacao_view, name='cotacao'),
]
