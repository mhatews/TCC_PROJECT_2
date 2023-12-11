from django.forms import ModelForm
from .models import Produto
from apps.categorias.models import Categoria
from apps.empresas.models import Empresa


class ProdutosForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ProdutosForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(empresa=user.empregado.empresa)

    
    class Meta:
        model = Produto
        fields = ['nome', 'categoria','valor_unitario']

