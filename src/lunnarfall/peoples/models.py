from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    # +5531999994444, (31) 99999-4444, 31999994444
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

class Cliente(Pessoa):
    dataCadastro = models.DateField()
    dataEntrada = models.DateField()
    dateSaida = models.DateField()
    despesaTotal = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO: colocar os relacionamento com a classe Reserva

class Funcionario(Pessoa):
    # TODO: User?
    dataAdmissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    # QUESTION: colocar opcoes para o cargo, e se aparecer novos cargos?
    cargo = models.CharField(max_length=40)


