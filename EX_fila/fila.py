from noPessoa import No
from pessoa import Pessoa

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0 

    def setInicio(self,inicio):
        self.inicio = inicio

    def setFim(self,fim):
        self.fim = fim 
    
    def setTamanho(self,tamanho):
        self.tamanho = tamanho

   
    def getInicio(self):
        return self.inicio
    
    def getFim(self):
        return self.fim 
    
    def getTamanho(self):
        return self.tamanho
    
 
    
    


        


    