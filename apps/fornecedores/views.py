from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fornecedor


class FornecedorList(ListView):
    models = Fornecedor

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Fornecedor.objects.filter(empresa=empresa_logada)
      return queryset

class FornecedorCreate(CreateView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_form.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('list_fornecedores')

    def form_valid(self, form):
      fornecedor  =  form.save(commit=False)
      fornecedor.empresa = self.request.user.empregado.empresa
      fornecedor.save()
      return super(FornecedorCreate, self).form_valid(form)
    
    
class FornecedorUpdate(UpdateView):
    model = Fornecedor
    template_name = 'fornecedores/fornecedor_form.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('list_fornecedores')

class FornecedorDelete(DeleteView):
   model = Fornecedor
   success_url = reverse_lazy('list_fornecedores')


