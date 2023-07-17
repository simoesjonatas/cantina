from django.urls import path
from .views import *

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('cardapio', cardapio_list, name='cardapio_list'),
    path('nova/', ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_delete'),
    # outras URLs do seu projeto
]
