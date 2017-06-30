from django.shortcuts import render
from django.views import generic

from .models import Quarto, Reserva

class QuartoIndexView(generic.ListView):
    template_name = 'quarto/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        all = Quarto.objects.all()
        response = {
            'name_header': 'Quarto(s)',
            'quartos': all,
        }
        return response

class QuartoDetailView(generic.DetailView):
    model = Quarto
    template_name = 'quarto/quarto_detail.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super(QuartoDetailView, self).get_context_data(**kwargs)
        return context

class ReservaIndexView(generic.ListView):
    template_name = 'quarto/reserva_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        all = Reserva.objects.all()
        response = {
            'name_header': 'Reserva(s)',
            'reservas': all,
        }
        return response