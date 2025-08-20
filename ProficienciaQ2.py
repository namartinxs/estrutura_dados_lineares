
# Parte 1: Declaração da Classe Produto

# 1. Declare a Classe Produto.
# a. Declare dois atributos privados: * __preco: do tipo float, para
# armazenar o valor do produto. * __estoque: do tipo int, para armazenar a quantidade disponível.
class Produto:
    # b. Crie um construtor (__init__) que receba e inicialize ambos os atributos.
    def __init__(self,preco:float,estoque:int):
        #  Adicione uma validação no construtor para garantir que o preço e o estoque iniciais não sejam negativos. Caso um valor negativo seja informado, inicialize com 0
        self._preco = preco if preco>=0 else 0.0
        self._estoque = estoque if estoque >= 0 else 0
    
    # c. Declare métodos de acesso para cada atributo: * get_preco(): retorna o valor do atributo __preco. * 

    def get_preco(self):
        return self._preco
    
    # set_preco(novo_preco): atualiza o valor do atributo __preco. O método não deve permitir a definição de um preço negativo; se um valor negativo for passado, o preço não deve ser alterado e uma mensagem de erro deve ser exibida. * 
    def set_preco(self, novo_preco: float):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço não pode ser negativo.")

# get_estoque(): retorna o valor do atributo __estoque. 
    def get_estoque(self):
        return self.__estoque
# * set_estoque(nova_quantidade): atualiza o
# valor do atributo __estoque. O método não deve permitir a definição de um estoque negativo.

    def set_estoque(self, nova_quantidade: int):
        if nova_quantidade >= 0:
            self.__estoque = nova_quantidade
        else:
            print("Erro: O estoque não pode ser negativo.")




# Parte 2: Programa de Utilização da Classe Produto
# 1. Implemente um programa principal que utilize a classe Produto para realizar as seguintes ações:
if __name__ == "__main__":
    # a. Instancie um objeto da classe Produto (por exemplo, um "Notebook Gamer"), definindo um preço e uma quantidade de estoque iniciais por meio do construtor.
    notGamer = Produto(8000.00,15)

# b. Mostre os valores iniciais dos atributos utilizando os métodos get. * Exemplo de saída: --- Valores Iniciais do Produto --- Preço: R$8000.00 Estoque: 15 unidades
    print("--- Valores Iniciais do Produto ---")
    print(f"Preço: R$ {notGamer.get_preco():.2f}")
    print(f"Estoque: {notGamer.get_estoque()} unidades") 

# c. Atualize os valores dos atributos utilizando os métodos set. Por exemplo, aumente o preço devido à alta do dólar e diminua o estoque após uma venda.
    notGamer.set_preco(8550.50)   # aumento do preço
    notGamer.set_estoque(14)      # venda de uma unidade

# d. Mostre os valores atualizados dos atributos para confirmar que as modificações foram aplicadas corretamente. * Exemplo de saída: ---Valores Atualizados do Produto --- Preço: R$ 8550.50 Estoque: 14 unidades
    print("\n--- Valores Atualizados do Produto ---")
    print(f"Preço: R$ {notGamer.get_preco():.2f}")
    print(f"Estoque: {notGamer.get_estoque()} unidades")

# e. Tente definir valores inválidos (um preço negativo e um
# estoque negativo) usando os métodos set e, em seguida, exiba os valores novamente para confirmar que a lógica de proteção da classe funcionou.

    notGamer.set_preco(-5000.00)   # preço inválido
    notGamer.set_estoque(-10)      # estoque inválido
    print("\n--- Após Tentativas de Atualização Inválida ---")
    print(f"Preço: R$ {notGamer.get_preco():.2f}")
    print(f"Estoque: {notGamer.get_estoque()} unidades")