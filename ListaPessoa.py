class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} | {self.idade} anos"
    
class ListaPessoas():
    def __init__(self):
        self.lista = []
    
    def inserir(self,pessoa):
        self.lista.append(pessoa)
    
    def remover(self, nome):
        for pessoa in self.lista:
            if pessoa.nome == nome:
                print(f"\nRemovendo {pessoa.nome}...\n")
                self.lista.remove(pessoa)
                return
            

    def buscar(self, nome):
        for pessoa in self.lista:
            if pessoa.nome == nome:
                return pessoa
            
        print(f"{nome} STATUS: Não encontrado")
        return None

    def percorrer(self):
        for pessoa in self.lista:
            print(pessoa)

# Programa principal
if __name__ == "__main__":
    lista = ListaPessoas()


    lista.inserir(Pessoa("Alice", 30))
    lista.inserir(Pessoa("Bob", 25))
    lista.inserir(Pessoa("Carlos", 40))


    lista.percorrer()


    # lista.remover("Bob")


    lista.percorrer()


    resultado = lista.buscar("Alice")
    if resultado:
        print("\n", resultado)
   
