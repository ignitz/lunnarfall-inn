from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    endereco = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Nome: ' + self.nome + ' CPF:' + self.cpf + '\n'


class Cliente(Pessoa):
    data_cadastro = models.DateField()
    despesa_total = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        response = 'Nome: ' + self.nome + ' CPF: ' + self.cpf + ' Despesa: ' + str(self.despesa_total) + '\n'
        return response


class Funcionario(Pessoa):
    CARGO = (
        ('C', 'Chefe'),
        ('M', 'Master'),
        ('J', 'Jedi'),
    )
    data_admissao = models.DateField()
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    cargo = models.CharField(max_length=1, choices=CARGO)
