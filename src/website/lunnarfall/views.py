from django.shortcuts import render
from django.views import generic
from pessoa.models import Cliente, Funcionario
from quarto.models import Quarto

class IndexView(generic.TemplateView):
    template_name = 'index.html'

def index_view(request):
    many_clientes = Cliente.objects.count()
    many_funcionarios = Funcionario.objects.count()
    many_rooms_available = Quarto.objects.filter(estado='Disponível').count()
    context = {
        'data': {
            'name_header': 'Início',
            'many_clientes': many_clientes,
            'many_funcionarios': many_funcionarios,
            'many_rooms_available': many_rooms_available,
        },
    }
    return render(request, 'index.html', context)