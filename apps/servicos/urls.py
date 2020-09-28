from django.urls import path
from .views import ListaCategoriaServico, EditarCategoriaServico

app_name = 'servicos'

urlpatterns = [
    path('categorias/', ListaCategoriaServico.as_view(), name='lista_categoria_servicos'),
    path('categoria/<slug:slug>/', EditarCategoriaServico.as_view(), name='edtar_categoria_servicos'),
]
