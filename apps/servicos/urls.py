from django.urls import path,include
from .views import ServicoList,ServicoCreate, ServicoUpdate, ServicoDelete

urlpatterns = [
    path('',ServicoList.as_view(), name='list_servicos'),
    path('novo',ServicoCreate.as_view(), name='create_servicos'),
    path('editar/<int:pk>',ServicoUpdate.as_view(), name='update_servicos'),
    path('deletar/<int:pk>',ServicoDelete.as_view(), name='delete_servicos'),
]
