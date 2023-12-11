from django.urls import path,include
from .views import EmpresaEdit

urlpatterns = [
    path('editar/<int:pk>',EmpresaEdit.as_view(), name='edit_empresa'),
]
