from django.urls import path
from produto.views import (
    home_produto, 
    view_criar_produto_get,
    view_criar_produto_post,
    view_atualizar_produto_get,
    view_atualizar_produto_post,
    view_editar_produto,
    view_vizualizar_produto, 
    view_deletar_produto
)

urlpatterns = [
    path('', home_produto, name='homeProduto'),
    path('criar/', view_criar_produto_get, name='view_criar_produto_get'),
    path('criar/post/', view_criar_produto_post, name='view_criar_produto_post'),
    path('<int:id>/', view_vizualizar_produto, name='view_vizualizar_produto'),
    path('<int:id>/editar/', view_editar_produto, name='view_editar_produto'),
    path('<int:id>/atualizar/', view_atualizar_produto_get, name='view_atualizar_produto_get'),
    path('<int:id>/atualizar/post/', view_atualizar_produto_post, name='view_atualizar_produto_post'),
    path('<int:id>/deletar/', view_deletar_produto, name='view_deletar_produto'),
]