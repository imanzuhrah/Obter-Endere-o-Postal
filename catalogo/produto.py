# Classe produto
class produto:

    # Método construtor de objetos
    def __init__ (self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        


    # Método para calcular desconto.
    def aplicar_desconto (self, percentual: float) -> float:

        desconto = self.preco * (percentual / 100)

        # Atribui o desconto e atualiza o preço do produto.
        self.preco = self.preco - desconto

        # Retorna o valor do desconto em reais
        return desconto
