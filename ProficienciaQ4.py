# Elabore um programa que:
# a. declare um vetor de inteiros de 10 posições,
# b. Preencha o mesmo com valores entre 20 e 50.
# c. Imprima o resultado da soma de todos os 10 valores preenchido
import random
vetor = [0]*10
#se nao for pra preencher todo o array
for i in range(len(vetor)):
    numero = random.randint(10,70)
    print(numero) 
    if(numero>=20 and numero<=50):
        vetor[i]=numero  

#se for pra preencher todo
# i = 0
# while i < 10:
#     numero = random.randint(10,70)
#     if(numero>=20 and numero<=50):
#         vetor[i]=numero
#         i+=1

print(vetor) 
print('soma',sum(vetor))
