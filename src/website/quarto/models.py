from django.db import models
from pessoa.models import Cliente

class Categoria(models.Model):
    NIVEL = (
        (1, 'Top'),
        (2, 'Topper'),
    )
    nome_categoria = models.IntegerField(choices=NIVEL)
    # TODO:
    # valor quarto podia ser gerado conforme o nivel
    valor_quarto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        response = 'Top' if self.nome_categoria == 1 else 'Topper'
        response += ', '
        response += str(self.valor_quarto)
        return response

class Quarto(models.Model):
    ESTADO = (
        ('Disponível', 'Disponível'),
        ('Ocupado', 'Ocupado'),
        ('Em faxina', 'Em faxina'),
    )
    numero = models.IntegerField()
    descricao_quarto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO)

    def __str__(self):
        response = str(self.numero) + ', ' + str(self.descricao_quarto) \
                   + ', ' + str(self.categoria) + ', ' + str(self.estado)
        return response

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)
    quarto = models.ForeignKey(Quarto, blank=True, null=True, on_delete=models.SET_NULL)
    data_reserva = models.DateField()
    num_diarias = models.IntegerField()
    # TODO: mais um atributo que pode ser gerado
    valor_reserva = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        response = str(self.cliente)
        return response

