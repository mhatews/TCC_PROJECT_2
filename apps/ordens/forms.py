from django.forms import inlineformset_factory
from .models import Ordem, ItemOrdem

ItemOrdemFormSet = inlineformset_factory(Ordem, ItemOrdem, fields=('servico', 'quantidade'), extra=1)

ItemOrdemUpdateFormSet = inlineformset_factory(Ordem, ItemOrdem, fields=('servico', 'quantidade'), extra=0)
