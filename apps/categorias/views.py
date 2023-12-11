from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

class CategoriaList(ListView):
    models = Categoria

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Categoria.objects.filter(empresa=empresa_logada)
      return queryset

class CategoriaCreate(CreateView):
    model = Categoria
    template_name = 'categorias/categoria_form.html'
    fields = ['nome']
    success_url = reverse_lazy('list_categorias')

    def form_valid(self, form):
      categoria  =  form.save(commit=False)
      categoria.empresa = self.request.user.empregado.empresa
      categoria.save()
      return super(CategoriaCreate, self).form_valid(form)
    
class CategoriaUpdate(UpdateView):
    model = Categoria
    template_name = 'categorias/categoria_form.html'
    fields = ['nome']
    success_url = reverse_lazy('list_categorias')

class CategoriaDelete(DeleteView):
   model = Categoria
   success_url = reverse_lazy('list_categorias')

