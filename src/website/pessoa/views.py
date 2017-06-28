# Para saber como funciona Generic Views
# https://www.youtube.com/watch?v=c3yB0_4Yd48&index=29&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
from django.views import generic

# from django.shortcuts import render
from .models import Cliente, Funcionario

# For join two QuerySets
from itertools import chain

class PessoaIndexView(generic.ListView):
    template_name = 'pessoa/index.html'
    context_object_name = 'all_people'

    def get_queryset(self):
        response = list(chain(Cliente.objects.all(), Funcionario.objects.all()))
        return response

class ClienteIndexView(PessoaIndexView):
    template_name = 'pessoa/cliente_list.html'
    def get_queryset(self):
        response = Cliente.objects.all()
        return response

class ClienteDetailView(generic.DetailView):
    model = Cliente
    template_name = 'detail.html'

class FuncionarioIndexView(PessoaIndexView):
    template_name = 'pessoa/funcionario_list.html'
    def get_queryset(self):
        response = Funcionario.objects.all()
        return response

class FuncionarioDetailView(generic.DetailView):
    model = Funcionario
    template_name = 'detail.html'

