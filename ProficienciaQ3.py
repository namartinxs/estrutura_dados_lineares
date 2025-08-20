# 3. Implemente um programa que receba como entrada somente números inteiros
# positivos e imprima apenas os que estejam no intervalo de 5 a 15. O Programa
# deve terminar quando for digitado o valor 0 

numeros = []
while True:
    entrada = input('numero?')
    if(entrada.isdigit()):
        numero = int(entrada)
        numeros.append(numero)
        if(numero==0):
            print('VOCE INSERIU ZERO. O PROGRAMA ACABA')
            break  
    else:
        print('só inteiros')
    
for i in range(len(numeros)):
    print('intervalo')
    if(numeros[i] >=5 and numeros[i]<=15):
        print(numeros[i])
    

