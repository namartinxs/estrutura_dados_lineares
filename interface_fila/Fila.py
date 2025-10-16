from no import No

class Fila:
    def __init__(self):
        self.__inicio= None
        self.__fim= None
        self.__tamanho= 0

    def setinicio(self, inicio):
        self.__inicio = inicio

    def getinicio(self):
        return self.__inicio
    
    def getFim(self):
        return self.__fim 
    
    def setFim(self, fim):
        self.__fim = fim

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho):
        self.__tamanho = tamanho    


    def enfilerar(self,valor):
        novo_no = No(valor)

        if self.__inicio is None:
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            self.__fim.setProximo(novo_no)
            novo_no.setAnterior(self.__fim)
            self.__fim = novo_no
        self.__tamanho += 1 

    def mostrar_fila (self):
        if self.__inicio is None:
            print('Vaziuuuu')
        else:
            self.mostrar_fila_rec(self.__inicio)

    def mostrar_fila_rec(self,no_atual):
            print(no_atual.getValor())
            if no_atual.getProximo() is not None:
                self.mostrar_fila_rec(no_atual.getProximo())

    def desenfilerar(self):
        if self.__inicio is None:
            print('Vaziuuuu')
        else: 
            self.__inicio.getProximo()
            valor = self.__inicio.getValor()
            self.__inicio = self.__inicio.getProximo()
            self.__tamanho = self.__tamanho -1
            return valor


