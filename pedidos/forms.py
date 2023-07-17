from django import forms
from .models import Pedido
from produtos.models import Produto

# class PedidoForm(forms.ModelForm):
#     produtos = forms.ModelMultipleChoiceField(queryset=Produto.objects.all(), widget=forms.CheckboxSelectMultiple)
#     quantidades = forms.CharField(widget=forms.HiddenInput())

#     class Meta:
#         model = Pedido
#         fields = ['nome_cliente', 'status_pedido', 'observacao', 'pagamento', 'produtos', 'quantidades']

#     def clean_quantidades(self):
#         quantidades = self.cleaned_data['quantidades']
#         quantidades = quantidades.split(',')
#         if len(quantidades) != len(self.cleaned_data['produtos']):
#             raise forms.ValidationError('Quantidades inválidas')
#         return quantidades

from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = []