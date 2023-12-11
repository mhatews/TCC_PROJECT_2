from django.urls import path,include
from .views import VendaList, VendaCreate, VendaUpdate, VendaDelete, VendaListFinanceiro

urlpatterns = [
    path('',VendaList.as_view(), name='list_vendas'),
    path('novo',VendaCreate.as_view(), name='create_vendas'),
    path('editar/<int:pk>',VendaUpdate.as_view(), name='update_vendas'),
    path('deletar/<int:pk>',VendaDelete.as_view(), name='delete_vendas'),
    path('deletar/<int:pk>',VendaDelete.as_view(), name='delete_vendas'),
    path('fincanceiro/',VendaListFinanceiro.as_view(), name='financeiro'),
]
