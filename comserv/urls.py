from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('empregados/', include('apps.empregados.urls')),
    path('produtos/', include('apps.produtos.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('fornecedores/', include('apps.fornecedores.urls')),
    path('vendas/', include('apps.vendas.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('empresa/', include('apps.empresas.urls')),
    path('servicos/', include('apps.servicos.urls')),
    path('ordens/', include('apps.ordens.urls')),
]
