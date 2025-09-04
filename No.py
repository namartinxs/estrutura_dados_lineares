class No:
    __valor:int
    __proximo:'No'

    def __init__(self,valor:int):
        self.__valor = valor
        self.__proximo=None

    def dfinValor(self,valor:int):
        self.__valor = valor 

    def dfinProximo(self,proximo:'No'):
        self.__proximo =proximo 

    def pegaVlor(self)->int:
        self.__valor

    def pegaProximo(self)->int:
        self.__proximo 

    def __str__(self):
        return print(str)