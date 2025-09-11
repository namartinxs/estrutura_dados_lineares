from No import No           
from Pessoa import Pessoa
class ListaPessoa:
    __inicio_lista:'No'
    __tamanho:int 

    def __init__(self):
        self.__inicio_lista = None 
        self.__tamanho = 0 

    def inserir(self,valor:Pessoa):
        self.__inserir(valor)
        self.__tamanho +=1

    def __inserir(self,valor:Pessoa):
        if self.__inicio_lista is None: 
            self.__inicio_lista = No(valor)
        else: 
            no_atual = self.__inicio_lista
            while no_atual.pegaProximo() is not None:
                no_atual = no_atual.pegaProximo() 

            no_atual.dfinProximo(No(valor))



    def listar_valores(self):
        if self.__inicio_lista is None:
            print( 'Lista vazia') 
            return 
        
        no_atual =  self.__inicio_lista
        while no_atual is not None:
            print(no_atual.pegaVlor()) 
            no_atual = no_atual.pegaProximo()
    
    def existe(self,valor)->bool:
        no_atual = self.__inicio_lista
        while no_atual is not None:
            if no_atual.pegaProximo()==valor:
                return True
            
        return  False

    def PesquisarNome(self, nome:str) -> bool:
        if self.__inicio_lista is None:
            print("lISTA VAZIA :(")
            return
        no_atual = self.__inicio_lista
        while no_atual is not None:
            if no_atual.pegaVlor().getNome()== nome:
                return True
            no_atual = no_atual.pegaProximo()
        return False 
    
    def apagarPorNome(self, nome:str) -> bool:
        # atual = self.__inicio_lista
        # anterior = None

        # while atual and atual.Pessoa.nome != nome:
        #     anterior = atual
        #     atual = atual.pegaProximo
        # if atual ==None:
        #     print('Pessoa não encontrada')
        #     return
        # if anterior is None:
        #     self.__inicio_lista == atual.pegaProximo
        # else:
        #     anterior.pegaProximo 
        if self.__inicio_lista == None:
            print('Lista vazia ')
            return False
        
        no_atual = self.__inicio_lista
        no_anterior = None 
        while no_atual is not None:
            if self.__inicio_lista.pegaVlor().getNome()== nome:
                if no_anterior == None:
                    self.__inicio_lista = no_atual.pegaProximo() 
                    return True 
                else:
                    no_anterior.dfiniProximo(no_atual.pegaProximo())
                    return True
            no_anterior = no_atual
            # no_atual = no_atual.pegaProximo()
            if no_atual == None:
                no_atual == None
            else:
                no_atual = no_atual.pegaProximo()

                return False

        return False


if __name__ == '__main__':
    lista = ListaPessoa()

    lista.inserir(Pessoa('j',12,1.51))
    lista.listar_valores()
    if lista.PesquisarNome('j'):
        print('existe')
    else:
        print('não existe')
    lista.apagarPorNome('j') 
    lista.listar_valores()


  
