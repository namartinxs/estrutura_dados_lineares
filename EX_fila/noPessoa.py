class No:
    def __init__(self,pessoa):
        self.proximo = None
        self.anterior = None
        self.pessoa = pessoa 

    def setProximaPessoa (self,proxima):
        self.proximo = proxima

    def getProxima(self):
        return self.proximo
    
    def setPessoaAnterior(self,anterior):
        self.anterior = anterior

    def getAnterior(self):
        return self.anterior 
    
    def setPessoa(self,pessoa):
        self.pessoa = pessoa 

    def getPessoa(self):
        return self.pessoa
    