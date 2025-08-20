# 6. Desafio FizzBuzz em Python
# Dado um número inteiro n, sua tarefa é criar um programa que itere de 1 até n. Para cada
# número nesse intervalo, imprima um valor em uma nova linha de acordo com as seguintes
# regras:
# • Se o número for um múltiplo de 3 e 5, imprima FizzBuzz.
# • Se o número for um múltiplo de 3 (mas não de 5), imprima Fizz.
# • Se o número for um múltiplo de 5 (mas não de 3), imprima Buzz.
# • Se o número não for múltiplo de 3 nem de 5, imprima o próprio número. 

# n = 10 
# for i in range(1,n):
#     if(i% 3==0 and i%5 ==0):
#         print('FizzBuzz') 
#     if(i% 3==0):
#         print('Fizz') 
#     if(i% 5==0):
#         print('Buzz') 
#     if(i% 3!=0 and i%5 !=0):
#         print(i)

#fun fizzbuzz

def fizzBuzz(limite):
    for i in range(1,limite):
        if(i% 3==0 and i%5 ==0):
            print('FizzBuzz') 
        if(i% 3==0):
            print('Fizz') 
        if(i% 5==0):
            print('Buzz') 
        if(i% 3!=0 and i%5 !=0):
            print(i) 

numero_escolhido = input('insira o numero')

fizzBuzz(int(numero_escolhido))
    

