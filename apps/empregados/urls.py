from django.urls import path,include
from .views import EmpregadosList,EmpregadosCreate, EmpregadosUpdate, EmpregadosDelete

urlpatterns = [
    path('',EmpregadosList.as_view(), name='list_empregados'),
    path('novo',EmpregadosCreate.as_view(), name='create_empregados'),
    path('editar/<int:pk>',EmpregadosUpdate.as_view(), name='edit_empregados'),
    path('deletar/<int:pk>',EmpregadosDelete.as_view(), name='delete_empregados'),
]
