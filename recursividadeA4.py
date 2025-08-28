def somaUm(numero):
    
    return numero + 1

#imprimir de 0 ate x
def ateAcondParada(parada): 
    numero = 0 
    
    while numero<= parada:
        print(numero)
        numero += somaUm(0)
        
        


#ateAcondParada(5)


def recursiva(n):
    if(n<0):
        return
    recursiva(n-1)
    print(n) 

recursiva(5)