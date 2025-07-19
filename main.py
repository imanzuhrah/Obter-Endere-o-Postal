# Importar o módulo de produto

from catalogo import produto


# Solicita o nome e o preço
nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto (R$): '))

meu_produto = produto(nome, preco)

print(meu_produto.nome)
print(meu_produto.preco)
