from django.urls import path,include
from .views import ProdutoList,ProdutoCreate, ProdutoUpdate, ProdutoDelete

urlpatterns = [
    path('',ProdutoList.as_view(), name='list_produtos'),
    path('novo',ProdutoCreate.as_view(), name='create_produtos'),
    path('editar/<int:pk>',ProdutoUpdate.as_view(), name='update_produtos'),
    path('deletar/<int:pk>',ProdutoDelete.as_view(), name='delete_produtos'),
]
