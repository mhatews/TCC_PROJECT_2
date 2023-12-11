from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Empregado
from django.contrib.auth.models import User

class EmpregadosList(ListView):
   model = Empregado

   def get_queryset(self):
      empresa_logada = self.request.user.empregado.empresa
      queryset = Empregado.objects.filter(empresa=empresa_logada)
      return queryset



class EmpregadosCreate(CreateView):
   model = Empregado
   template_name = 'empregados/empregado_form.html'
   fields = ['nome']
   success_url = reverse_lazy('list_empregados')

   def form_valid(self, form):
      empregado  =  form.save(commit=False)
      username = empregado.nome.split(' ')[0] + empregado.nome.split(' ')[1]
      empregado.empresa = self.request.user.empregado.empresa
      empregado.user = User.objects.create(username= username)
      empregado.save()
      return super(EmpregadosCreate, self).form_valid(form)

class EmpregadosUpdate(UpdateView):
   model = Empregado
   template_name = 'empregados/empregado_form.html'
   fields = ['nome', 'user', 'empresa']
   success_url = reverse_lazy('list_empregados')

class EmpregadosDelete(DeleteView):
   model = Empregado
   success_url = reverse_lazy('list_empregados')




