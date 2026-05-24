# seu_app/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Produto")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, verbose_name="Preço")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")

    def __str__(self):
        return self.nome
      # seu_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto

# 1. LISTAGEM (Com Filtro de Busca e Paginação)
def listar_produtos(request):
    lista_produtos = Produto.objects.all().order_by('nome')
    
    # Lógica de Busca (Desafio Extra)
    busca = request.GET.get('busca')
    if busca:
        lista_produtos = lista_produtos.filter(nome__icontains=busca)
        
    # Lógica de Paginação - Exemplo: 5 produtos por página (Desafio Extra)
    paginador = Paginator(lista_produtos, 5)
    numero_pagina = request.GET.get('page')
    produtos_paginados = paginador.get_page(numero_pagina)
    
    return render(request, 'produtos/listar.html', {'produtos': produtos_paginados, 'busca': busca})

# 2. CADASTRO
def cadastrar_produto(request):
    if request.method == "POST":
        Produto.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            quantidade=request.POST.get('quantidade')
        )
        return redirect('listar_produtos')
    return render(request, 'produtos/formulario.html')

# 3. ATUALIZAÇÃO
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/formulario.html', {'produto': produto})

# 4. EXCLUSÃO
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})
  # seu_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Controle de Produtos</title>
</head>
<body>
    <h1>Gerenciamento de Produtos</h1>
    
    <a href="{% url 'cadastrar_produto' %}" style="font-weight: bold;">+ Cadastrar Novo Produto</a>
    <br><br>

    <form method="GET" action="{% url 'listar_produtos' %}">
        <input type="text" name="busca" placeholder="Buscar produto por nome..." value="{{ busca|default:'' }}">
        <button type="submit">Pesquisar</button>
        {% if busca %}
            <a href="{% url 'listar_produtos' %}">Limpar filtro</a>
        {% endif %}
    </form>

    <br>

    <table border="1" cellpadding="5" cellspacing="0">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Descrição</th>
                <th>Preço</th>
                <th>Quantidade</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for produto in produtos %}
            <tr>
                <td>{{ produto.nome }}</td>
                <td>{{ produto.descricao|default:"-" }}</td>
                <td>R$ {{ produto.preco }}</td>
                <td>{{ produto.quantidade }} unid.</td>
                <td>
                    <a href="{% url 'editar_produto' produto.pk %}">Editar</a> | 
                    <a href="{% url 'excluir_produto' produto.pk %}">Excluir</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5">Nenhum produto cadastrado ou encontrado.</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <br>
    <div>
        {% if produtos.has_previous %}
            <a href="?page=1{% if busca %}&busca={{ busca }}{% endif %}">&laquo; Primeira</a>
            <a href="?page={{ produtos.previous_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Anterior</a>
        {% endif %}

        <span>Página {{ produtos.number }} de {{ produtos.paginator.num_pages }}</span>

        {% if produtos.has_next %}
            <a href="?page={{ produtos.next_page_number }}{% if busca %}&busca={{ busca }}{% endif %}">Próxima</a>
            <a href="?page={{ produtos.paginator.num_pages }}{% if busca %}&busca={{ busca }}{% endif %}">Última &raquo;</a>
        {% endif %}
    </div>
</body>
</html>
# seu_app/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Produto

class ProdutoModelAndUrlTest(TestCase):

    def setUp(self):
        # Cria um produto de exemplo no banco de dados de teste
        self.produto = Produto.objects.create(
            nome="Teclado Mecânico",
            descricao="Teclado RGB switch azul",
            preco=250.00,
            quantidade=10
        )

    def test_criacao_do_produto(self):
        """Valida se o produto foi inserido e os dados estão corretos."""
        item = Produto.objects.get(id=self.produto.id)
        self.assertEqual(item.nome, "Teclado Mecânico")
        self.assertEqual(item.quantidade, 10)

    def test_status_code_da_listagem(self):
        """Garante que a rota principal de listagem responde com sucesso (200)."""
        resposta = self.client.get(reverse('listar_produtos'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Teclado Mecânico")
