from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoList(ListView):
    model = Produto

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Produto.objects.filter(empresa=empresa_logada)
      return queryset

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produtos/produto_form.html'
    fields = ['nome', 'categoria','valor_unitario']
    success_url = reverse_lazy('list_produtos')

    def form_valid(self, form):
      produto  =  form.save(commit=False)
      produto.empresa = self.request.user.empregado.empresa
      produto.save()
      return super(ProdutoCreate, self).form_valid(form)
    
    
class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produtos/produto_form.html'
    fields = ['nome', 'categoria','valor_unitario']
    success_url = reverse_lazy('list_produtos')

class ProdutoDelete(DeleteView):
   model = Produto
   success_url = reverse_lazy('list_produtos')