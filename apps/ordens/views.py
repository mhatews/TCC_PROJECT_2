from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ordem, ItemOrdem
from .forms import ItemOrdemFormSet, ItemOrdemUpdateFormSet
from django.db.models import Sum


class OrdemList(ListView):
    models = Ordem

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Ordem.objects.filter(empresa=empresa_logada)
      return queryset
    

class OrdemCreate(CreateView):
    model = Ordem
    template_name = 'ordens/ordem_form.html'
    fields = ['cliente', 'data', 'status']
    success_url = reverse_lazy('list_ordens')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ItemOrdemFormSet(self.request.POST)
        else:
            data['formset'] = ItemOrdemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Salve a instância principal
        self.object = form.save(commit=False)
        self.object.empresa = self.request.user.empregado.empresa
        self.object.save()

        #calcular_valor_total(self.object)

        # Associe instâncias relacionadas à instância principal
        if formset.is_valid():
            for form in formset:
                item = form.save(commit=False)
                item.ordem = self.object
                item.save()

        self.object.calcular_valor_total()

        return super(OrdemCreate, self).form_valid(form)
    
class OrdemUpdate(UpdateView):
    model = Ordem
    template_name = 'ordens/ordem_form.html'
    fields = ['cliente', 'data', 'status']
    success_url = reverse_lazy('list_ordens')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ItemOrdemUpdateFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = ItemOrdemUpdateFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Salve a instância principal
        self.object = form.save(commit=False)
        self.object.empresa = self.request.user.empregado.empresa
        self.object.save()


        # Associe instâncias relacionadas à instância principal
        if formset.is_valid():
            for form in formset:
                item = form.save(commit=False)
                item.ordem = self.object
                item.save()

        self.object.calcular_valor_total()

        return super(OrdemUpdate, self).form_valid(form)
    

class OrdemDelete(DeleteView):
   model = Ordem
   success_url = reverse_lazy('list_ordens')

class OrdemListFinanceiro(ListView):
    model = Ordem
    template_name = 'ordens/financeiro_ordens.html'

    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        queryset = Ordem.objects.filter(empresa=empresa_logada)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa_logada = self.request.user.empregado.empresa

        # Calcule o total de vendas a receber
        total_a_receber = Ordem.objects.filter(
            empresa=empresa_logada,
            status__nome='A RECEBER',
            data_recebimento__isnull=True  # Apenas vendas não pagas
        ).aggregate(Sum('valor_total'))['valor_total__sum'] or 0

        context['total_a_receber'] = total_a_receber
        return context


