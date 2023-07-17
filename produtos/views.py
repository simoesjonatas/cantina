from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'produtos'
    paginate_by = 10

class ProdutoCreateView(CreateView):
    model = Produto
    fields = '__all__' 
    success_url = reverse_lazy('produto_list')

class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = 'produto'

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = '__all__' 
    context_object_name = 'produto'

    def get_success_url(self):
        return reverse_lazy('produto_detail', kwargs={'pk': self.object.pk})

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')
    context_object_name = 'produto'

def cardapio_list(request):
    produtos = Produto.objects.filter(disponivel=True,quantidade_estoque__gt=0)
    return render(request, 'produtos/cardapio.html', {'produtos': produtos})
