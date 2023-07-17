from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Pedido, ItemPedido
from .forms import PedidoForm
from produtos.models import Produto


def listar_pedidos(request):
    pedidos_preparando = Pedido.objects.filter(status_pedido='preparando')
    pedidos_pronto = Pedido.objects.filter(status_pedido='pronto')
    return render(request, 'pedidos/pedidos.html', {'pedidos_preparando': pedidos_preparando, 'pedidos_pronto': pedidos_pronto})

def vitrine(request):
    produtos = Produto.objects.all()
    form = PedidoForm()
    return render(request, 'pedidos/vitrine.html', {'produtos': produtos, 'form': form})

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            
            produtos_ids = request.POST.getlist('produtos')
            for produto_id in produtos_ids:
                produto = Produto.objects.get(id=produto_id)
                ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=1)
            
            return redirect('pagina_sucesso')
    else:
        form = PedidoForm()
    
    produtos = Produto.objects.all()
    return render(request, 'vitrine.html', {'form': form, 'produtos': produtos})

# View de listagem de pedidos
class PedidoListView(ListView):
    model = Pedido
    context_object_name = 'pedidos'

# View de detalhes de um pedido
class PedidoDetailView(DetailView):
    model = Pedido
    context_object_name = 'pedido'

# View de criação de um pedido
class PedidoCreateView(View):
    def get(self, request):
        form = PedidoForm()
        return render(request, 'pedidos/pedido_create.html', {'form': form})
    
    def post(self, request):
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            # Processar produtos e quantidades
            produtos = form.cleaned_data['produtos']
            quantidades = request.POST.getlist('quantidades')
            for produto, quantidade in zip(produtos, quantidades):
                ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)
            return redirect('pedido_detail', pk=pedido.pk)
        return render(request, 'pedidos/pedido_create.html', {'form': form})

# View de atualização de um pedido
class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ['nome_cliente', 'status_pedido', 'observacao', 'pagamento']

# View de exclusão de um pedido
class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = '/pedidos/'  # URL para redirecionamento após exclusão bem-sucedida
