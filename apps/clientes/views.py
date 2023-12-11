from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente

class ClienteList(ListView):
    models = Cliente

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Cliente.objects.filter(empresa=empresa_logada)
      return queryset

class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome', 'telefone', 'cpf_cnpj', 'rua', 'bairro', 'cidade', 'cep']
    success_url = reverse_lazy('list_clientes')

    def form_valid(self, form):
      cliente  =  form.save(commit=False)
      cliente.empresa = self.request.user.empregado.empresa
      cliente.save()
      return super(ClienteCreate, self).form_valid(form)
    
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nome', 'telefone', 'cpf_cnpj', 'rua', 'bairro', 'cidade', 'cep']
    success_url = reverse_lazy('list_clientes')

class ClienteDelete(DeleteView):
   model = Cliente
   success_url = reverse_lazy('list_clientes')
