class Estrutura:
    def __init__(self):
        self.__dados = []
        self.__limite = 10
        self.__escape = 5
        self.__inicio = 0  

    def addElemento(self, valor):
        if len(self.__dados) < self.__limite:
            self.__dados.append(valor)
        else:
            # fila circular 
            self.__dados[self.__inicio] = valor
            self.__inicio = (self.__inicio + 1) % self.__limite

        if len(self.__dados) > self.__escape and len(self.__dados) < self.__limite:
            print("Aviso: já existem mais de 5 elementos armazenados.")
        elif len(self.__dados) == self.__limite:
            print("Aviso: a lista chegou a 10 elementos. Novos valores sobrescrevem os antigos.")

    def removeElemento(self, valor):
        if valor in self.__dados:
            self.__dados.remove(valor)
        else:
            print("Valor não encontrado.")

    def removerPosicao(self, posicao):
        if 0 <= posicao < len(self.__dados):
            self.__dados.pop(posicao)
        else:
            print("Posição inválida.")

    def showElementos(self):
        for i, v in enumerate(self.__dados):
            print(f"Posição {i}: {v}")

    def tamanho(self):
        return len(self.__dados)

    def espacosLivres(self):
        return self.__limite - len(self.__dados)

    def existe(self, valor):
        return valor in self.__dados

    def limpar(self):
        self.__dados.clear()
        self.__inicio = 0
        print("Todos os dados foram apagados.")

# Programa principal (teste)
if __name__ == "__main__":
    ed = Estrutura()

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar valor")
        print("2 - Remover valor")
        print("3 - Remover por posição")
        print("4 - Mostrar elementos")
        print("5 - Mostrar tamanho e espaços livres")
        print("6 - Verificar se valor existe")
        print("7 - Limpar todos os dados")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor: "))
            ed.addElemento(valor)

        elif opcao == "2":
            valor = int(input("Digite o valor a remover: "))
            ed.removeElemento(valor)

        elif opcao == "3":
            pos = int(input("Digite a posição a remover: "))
            ed.removerPosicao(pos)

        elif opcao == "4":
            print("\nElementos armazenados:")
            ed.showElementos()

        elif opcao == "5":
            print(f"Tamanho: {ed.tamanho()} | Espaços livres: {ed.espacosLivres()}")

        elif opcao == "6":
            valor = int(input("Digite o valor para verificar: "))
            print("Existe na lista?", ed.existe(valor))

        elif opcao == "7":
            ed.limpar()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida, tente novamente!")
