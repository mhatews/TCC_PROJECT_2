from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Servico

class ServicoList(ListView):
    models = Servico

    def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Servico.objects.filter(empresa=empresa_logada)
      return queryset

class ServicoCreate(CreateView):
    model = Servico
    template_name = 'servicos/servico_form.html'
    fields = ['nome', 'valor_uni']
    success_url = reverse_lazy('list_servicos')

    def form_valid(self, form):
      servico  =  form.save(commit=False)
      servico.empresa = self.request.user.empregado.empresa
      servico.save()
      return super(ServicoCreate, self).form_valid(form)
    
class ServicoUpdate(UpdateView):
    model = Servico
    template_name = 'servicos/servico_form.html'
    fields = ['nome', 'valor_uni']
    success_url = reverse_lazy('list_servicos')

class ServicoDelete(DeleteView):
   model = Servico
   success_url = reverse_lazy('list_servicos')
