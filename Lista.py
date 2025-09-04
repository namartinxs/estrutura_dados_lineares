from No import No
class Lista:
    __inicio_lista:'No'
    __tamanho:int 

    def __init__(self):
        self.__inicio_lista = None 
        self.__tamanho = 0 

    def inserir(self,valor:int):
        self.__inserir(valor)
        self.__tamanho +=1

    def __inserir(self,valor:int):
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


if __name__ == '__main__':
    lista = Lista()

    lista.inserir(1)
    lista.inserir(2)
    lista.inserir(3)
