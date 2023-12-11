from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Venda, ItemVenda
from .forms import ItemVendaFormSet
from django.db.models import Sum

class VendaList(ListView):
    models = Venda

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Venda.objects.filter(empresa=empresa_logada)
      return queryset
    

class VendaCreate(CreateView):
    model = Venda
    template_name = 'vendas/venda_form.html'
    fields = ['cliente', 'data']
    success_url = reverse_lazy('list_vendas')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ItemVendaFormSet(self.request.POST)
        else:
            data['formset'] = ItemVendaFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Salve a instância principal
        self.object = form.save()

        # Associe instâncias relacionadas à instância principal
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super(VendaCreate, self).form_valid(form)
        else:
            return self.form_invalid(form)
    
class VendaUpdate(UpdateView):
    model = Venda
    template_name = 'vendas/venda_form.html'
    fields = ['cliente', 'data']
    success_url = reverse_lazy('list_vendas')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ItemVendaFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = ItemVendaFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        venda = form.save(commit=False)
        venda.empresa = self.request.user.empregado.empresa
        venda.save()
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super(VendaUpdate, self).form_valid(form)
        else:
            return self.form_invalid(form)


class VendaDelete(DeleteView):
   model = Venda
   success_url = reverse_lazy('list_vendas')


from django.db.models import Sum
from django.views.generic import ListView
from .models import Venda, ItemVenda

class VendaListFinanceiro(ListView):
    model = Venda
    template_name = 'vendas/financeiro_list.html'

    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        queryset = Venda.objects.filter(empresa=empresa_logada)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_logada = self.request.user.empregado.empresa

        # Calcule o total de vendas a receber
        total_a_receber = Venda.objects.filter(
            empresa=empresa_logada,
            data_recebimento__isnull=True  # Apenas vendas não pagas
        ).aggregate(Sum('valor_total'))['valor_total__sum'] or 0

        context['total_a_receber'] = total_a_receber
        return context
