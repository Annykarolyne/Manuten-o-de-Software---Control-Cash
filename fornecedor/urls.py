from django.urls import path
from .views import (
    listar_fornecedores, 
    cadastrar_fornecedor_get,
    cadastrar_fornecedor_post,
    atualizar_fornecedor, 
    vizualizar_fornecedor, 
    deletar_fornecedor
)

urlpatterns = [
    path('listar/', listar_fornecedores, name='fornecedor_listar'),
    path('cadastrar/', cadastrar_fornecedor_get, name='fornecedor_cadastrar'),
    path('cadastrar/post/', cadastrar_fornecedor_post, name='cadastrar_fornecedor_post'),
    path('atualizar/<int:id>/', atualizar_fornecedor, name='fornecedor_atualizar'),
    path('vizualizar/<int:id>/', vizualizar_fornecedor, name='fornecedor_vizualizar'),
    path('deletar/<int:id>/', deletar_fornecedor, name='fornecedor_deletar'),
]