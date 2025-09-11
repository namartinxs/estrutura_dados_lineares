from Pessoa import Pessoa

class No:
    __valor:Pessoa
    __proximo:'No'

    def __init__(self,valor:Pessoa):
        self.__valor = valor
        self.__proximo=None

    def dfiniValor(self,valor:Pessoa):
        self.__valor = valor 

    def dfiniProximo(self,proximo:'No'):
        self.__proximo =proximo 

    def pegaVlor(self)->Pessoa:
        return self.__valor

    def pegaProximo(self)->'No':
       return self.__proximo 

    def __str__(self):
        return str(self.__valor)