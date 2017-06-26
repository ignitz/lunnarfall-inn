from django.views import generic
from pessoa.models import Cliente

class IndexView(generic.ListView):
    template_name = 'index.html'
    # Por padrao eh object_list, mas da pra mudar os nomes aqui
    context_object_name = 'all_clientes'

    def get_queryset(self):
        return Cliente.objects.all()

class DetailView(generic.DetailView):
    model = Cliente
    template_name = 'detail.html'