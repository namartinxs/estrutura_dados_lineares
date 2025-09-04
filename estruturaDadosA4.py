

class Estrutura:
    def __init__(self):
        self.__dados=[]
        self.__limite =10
        self.__escape = 5

    # def deleteOption():
    #    resposta = questionary.select("Você deseja apagar algum numero?",choices=["Sim","Não"]).ask() 
    #    return resposta == "Sim" 
    
    def removeElementos(self,valor): 
        if valor in self.__dados:
          self.__dados.pop(valor)
        else:
          raise ValueError("Valor fora da lista") 
        
    def showElementos(self):
       vet = self.__dados.copy() 
       for i in range(len(vet)):
        print("Número: ",vet[i],"POSIÇÃO",i)
    
    def addElementos(self,valores):
         if len(self.__dados) > 10:
            # Substitui os elementos existentes pelos novos valores, mantendo o tamanho da lista
            for i in range(min(len(self.__dados), len(valores))):
                self.__dados[i] = valores[i]
         else:
            # Se não tiver mais que 10 elementos, apenas adiciona os valores
            self.__dados.append(valores)

    def tamanho(self):
        return len(self.__dados) 
    
    def verificadora(__self):
        qtd = len(__self.__dados)
        if qtd > __self.__escape or qtd == __self.__limite:
         result = "5 elementos" if qtd > 5 else "10 elementos" if qtd == 10 else ""
         print("Sua lista possui mais de", result)  


if __name__ == "__main__": 
   pass


