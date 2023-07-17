from django.db import models
from categorias.models import Categoria

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    descricao = models.TextField('Descrição do Produto', blank=True)
    disponivel = models.BooleanField(default=True)
    quantidade_estoque = models.IntegerField('Quantidade no Estoque', default= 0)
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to='produtos', blank=True)
    data_criacao = models.DateTimeField("data criação", auto_now_add=True)


    def __str__(self):
        return self.nome + ' - ' +  str(self.preco)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)