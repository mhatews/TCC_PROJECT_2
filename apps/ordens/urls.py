from django.urls import path,include
from .views import OrdemList, OrdemCreate, OrdemUpdate, OrdemDelete, OrdemListFinanceiro

urlpatterns = [
    path('',OrdemList.as_view(), name='list_ordens'),
    path('novo',OrdemCreate.as_view(), name='create_ordens'),
    path('editar/<int:pk>',OrdemUpdate.as_view(), name='update_ordens'),
    path('deletar/<int:pk>',OrdemDelete.as_view(), name='delete_ordens'),
    path('fincanceiro/',OrdemListFinanceiro.as_view(), name='financeiro_ordens'),
    
]
