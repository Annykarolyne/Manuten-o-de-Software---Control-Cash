from django.urls import path
from .views import (
    listar_fornecedores, 
    cadastrar_fornecedor_get,
    cadastrar_fornecedor_post,
    atualizar_fornecedor_get, 
    atualizar_fornecedor_post,
    vizualizar_fornecedor, 
    deletar_fornecedor_get,
    deletar_fornecedor_post
)

urlpatterns = [
    path('listar/', listar_fornecedores, name='fornecedor_listar'),
    path('cadastrar/', cadastrar_fornecedor_get, name='fornecedor_cadastrar'),
    path('cadastrar/post/', cadastrar_fornecedor_post, name='cadastrar_fornecedor_post'),
    path('atualizar/<int:id>/', atualizar_fornecedor_get, name='fornecedor_atualizar'),
    path('atualizar/<int:id>/post/', atualizar_fornecedor_post, name='atualizar_fornecedor_post'),
    path('vizualizar/<int:id>/', vizualizar_fornecedor, name='fornecedor_vizualizar'),
    # rota GET para exibir a página de exclusão
    path('deletar/<int:id>/', deletar_fornecedor_get, name='fornecedor_deletar'),
    # rota POST para executar a exclusão
    path('deletar/<int:id>/post/', deletar_fornecedor_post, name='deletar_fornecedor_post'),
]