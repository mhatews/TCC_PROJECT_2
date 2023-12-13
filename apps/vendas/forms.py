from django.forms import inlineformset_factory
from .models import Venda, ItemVenda


ItemVendaFormSet = inlineformset_factory(Venda, ItemVenda, fields=('produto', 'quantidade'), extra=1)

ItemVendaUpdateFormSet = inlineformset_factory(Venda, ItemVenda, fields=('produto', 'quantidade'), extra=1)



