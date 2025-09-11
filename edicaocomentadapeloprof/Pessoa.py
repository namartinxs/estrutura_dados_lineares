#edicao comentada pelo prof

class Pessoa:
    __nome:str
    __idade:int
    __altura:float
 
    def __init__(self,nome,idade,altura):
        self.__idade = idade 
        self.__nome = nome
        self.__altura = altura

    #interface publica da classe  Pessoa 
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getAltura(self):
        return self.__altura
    
    def setNome(self,nome:str):
        self.__nome=nome
    def setIdade(self,idade:int):
        self.__idade=idade
    def setAltura(self,altura:float):
        self.__altura=altura


    def __str__(self):
        return f"Nome {self.__nome} Idade {self.__idade} aLtura {self.__altura}"