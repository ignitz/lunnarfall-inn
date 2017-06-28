from django.shortcuts import render
from django.views import generic
from pessoa.models import Cliente, Funcionario

class IndexView(generic.TemplateView):
    template_name = 'index.html'

def index_view(request):
    many_clientes = Cliente.objects.count()
    many_funcionarios = Funcionario.objects.count()
    context = {
        'many_clientes': many_clientes,
        'many_funcionarios': many_funcionarios,
    }
    return render(request, 'index.html', context)