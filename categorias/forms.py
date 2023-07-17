from django.forms import ModelForm
from .models import categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = categoria
        fields = "__all__"