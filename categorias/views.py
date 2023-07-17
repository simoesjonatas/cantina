from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

class CategoriaListView(ListView):
    model = Categoria
    # template_name = 'categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

class CategoriaCreateView(CreateView):
    model = Categoria
    # template_name = 'categoria_form.html'
    fields = ['nome', 'foto']
    # fields = ['nome']
    success_url = reverse_lazy('categoria_list')

class CategoriaDetailView(DetailView):
    model = Categoria
    # template_name = 'categoria_detail.html'
    context_object_name = 'categoria'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    # template_name = 'categoria_form.html'
    fields = ['nome', 'foto']
    # fields = ['nome']
    context_object_name = 'categoria'

    def get_success_url(self):
        return reverse_lazy('categoria_detail', kwargs={'pk': self.object.pk})

class CategoriaDeleteView(DeleteView):
    model = Categoria
    # template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')
    context_object_name = 'categoria'
