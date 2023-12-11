from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Empresa




class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']

