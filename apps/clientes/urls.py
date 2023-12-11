from django.urls import path,include
from .views import ClienteList,ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    path('',ClienteList.as_view(), name='list_clientes'),
    path('novo',ClienteCreate.as_view(), name='create_clientes'),
    path('editar/<int:pk>',ClienteUpdate.as_view(), name='update_clientes'),
    path('deletar/<int:pk>',ClienteDelete.as_view(), name='delete_clientes'),
]
