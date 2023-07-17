from django.urls import path
from .views import *

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/', listar_pedidos, name='listar_pedidos'),
    path('vitrine/', vitrine, name='vitrine'),
    path('cadastrar-pedido/', cadastrar_pedido, name='cadastrar_pedido'),

    path('<int:pk>/', PedidoDetailView.as_view(), name='pedido_detail'),
    path('create/', PedidoCreateView.as_view(), name='pedido_create'),
    path('update/<int:pk>/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('delete/<int:pk>/', PedidoDeleteView.as_view(), name='pedido_delete'),
]
