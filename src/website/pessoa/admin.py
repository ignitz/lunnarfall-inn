from django.contrib import admin

from .models import Cliente, Funcionario

admin.site.register(Cliente)
admin.site.register(Funcionario)