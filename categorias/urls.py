from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaDetailView, CategoriaUpdateView, CategoriaDeleteView

urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria_list'),
    path('nova/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('<int:pk>/excluir/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    # outras URLs do seu projeto
]
