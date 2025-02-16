from django.forms import ModelForm
from .models import Produto

class CadastrarProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_venda', 'descricao', 'quantidade_estoque']
