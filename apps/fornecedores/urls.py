from django.urls import path,include
from .views import FornecedorList,FornecedorCreate, FornecedorUpdate, FornecedorDelete

urlpatterns = [
    path('',FornecedorList.as_view(), name='list_fornecedores'),
    path('novo',FornecedorCreate.as_view(), name='create_fornecedores'),
    path('editar/<int:pk>',FornecedorUpdate.as_view(), name='update_fornecedores'),
    path('deletar/<int:pk>',FornecedorDelete.as_view(), name='delete_fornecedores'),
]
