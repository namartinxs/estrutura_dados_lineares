class No:
    def __init__(self, valor):
        self.proximo= None
        self.anterior= None
        self.valor= valor
    
    def setProximo(self, proximo):
        self.proximo = proximo

    def getProximo(self):
        return self.proximo
    
    def getAnterior(self):
        return self.anterior 
    
    def setAnterior(self, anterior):
        self.anterior = anterior

    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor) 
    

