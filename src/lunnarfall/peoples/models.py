# TODO: para codificar acessos a quatos, talvez nao seja aqui
from django.contrib.auth.models import Permission, User

from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

class Pessoa(models.Model):
    # TODO: User?
    nome = models.CharField(max_length=200)
    # +5531999994444, (31) 99999-4444, 31999994444
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE, # TODO: verificar se realmente eh assim
    )


class Cliente(Pessoa):
    dataCadastro = models.DateField()
    dataEntrada = models.DateField()
    dateSaida = models.DateField()
    despesaTotal = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO: colocar os relacionamento com a classe Reserva

class Funcionario(Pessoa):
    dataAdmissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    # QUESTION: colocar opcoes para o cargo, e se aparecer novos cargos?
    cargo = models.CharField(max_length=40)


