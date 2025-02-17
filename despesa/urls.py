from django.urls import path
from despesa.views import (
    listar_despesas_view,
    criar_despesa_get_view,
    criar_despesa_post_view,
    editar_despesa_get_view,
    editar_despesa_post_view,
    remover_despesa_view
)

app_name = 'despesa'

urlpatterns = [
    path('', listar_despesas_view, name='despesa_listar'),
    path('criar/', criar_despesa_get_view, name='despesa_criar_get'),
    path('criar/post/', criar_despesa_post_view, name='despesa_criar_post'),
    path('<int:pk>/editar/', editar_despesa_get_view, name='despesa_editar_get'),
    path('<int:pk>/editar/post/', editar_despesa_post_view, name='despesa_editar_post'),
    path('<int:pk>/remover/', remover_despesa_view, name='despesa_remover'),
]
