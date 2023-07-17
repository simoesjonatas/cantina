from django.db import models
from django.urls import reverse
import os

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    foto = models.ImageField(upload_to='categorias', blank=True)
    data_criacao = models.DateTimeField("data criação", auto_now_add=True)


    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('categoria-detail', args=[str(self.id)])


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)