class Pessoa:
    def __init__(self,nome,prioridade):
        self.prioridade  = prioridade
        self.nome = nome

    def getPrioridade (self):
        return self.prioridade 
    
    # def setPrioridade(self,prioridade): 
    #     self.prioridade = prioridade

    def __str__(self):
        return f"{self.nome} (prioridade {self.prioridade})"
  