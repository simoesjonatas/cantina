from django.db import models

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )
    
    PAGAMENTO_CHOICES = (
        ('dinheiro', 'Dinheiro'),
        ('pix', 'PIX'),
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
        ('vale', 'Vale'),
    )

    nome_cliente = models.CharField(max_length=100)
    status_pedido = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparando')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    observacao = models.TextField(blank=True)
    pagamento = models.CharField(max_length=20, choices=PAGAMENTO_CHOICES)

    produtos = models.ManyToManyField('produtos.Produto', through='ItemPedido')
    
    def atualizar_total(self):
        self.total = sum(item.produto.preco * item.quantidade for item in self.itempedido_set.all())
        self.save()

    def __str__(self):
        return f"Pedido #{self.pk} - {self.nome_cliente}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.pedido.atualizar_total()

    def __str__(self):
        return f"{self.produto.nome} - Quantidade: {self.quantidade}"

