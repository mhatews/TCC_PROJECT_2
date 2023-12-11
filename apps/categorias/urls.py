from django.urls import path,include
from .views import CategoriaList,CategoriaCreate, CategoriaUpdate, CategoriaDelete

urlpatterns = [
    path('',CategoriaList.as_view(), name='list_categorias'),
    path('novo',CategoriaCreate.as_view(), name='create_categorias'),
    path('editar/<int:pk>',CategoriaUpdate.as_view(), name='edit_categorias'),
    path('deletar/<int:pk>',CategoriaDelete.as_view(), name='delete_categorias'),
]
