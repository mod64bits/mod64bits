from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import CategoriaServicos


class NovoServicoView(CreateView):
    model = CategoriaServicos
    context_object_name = 'categoriaServicos'
    template_name = 'servicos/nova_categoria_servico.html'


class ListaCategoriaServico(ListView):
    model = CategoriaServicos
    template_name = 'servicos/lista_categoria_servico.html'


class EditarCategoriaServico(UpdateView):
    model = CategoriaServicos
    fields = '__all__'
    template_name = 'servicos/editar_categoria_servico.html'
