import random
import math
# a. Declare um vetor de inteiros de 10 posições
vetor = [0]*10
# b. Preencha o vetor
i=0
while i < 10:
    numero = random.randint(10,70)
    if(numero>=20 and numero<=50):
        vetor[i]=numero
        i+=1
print(vetor)
# c. Imprima os valores do vetor de maneira invertida, do último elemento
# pra primeiro;
# stop = 9
# while stop >=0:
#     print(vetor[stop])
#     stop-=1


# d. mostre o maior e o menor valor do vetor
# menor = math.inf
# maior = -math.inf
# for i in range(len(vetor)):
#     if (vetor[i]> maior):
#         maior= vetor[i]
#     if(vetor[i]<menor):
#         menor=vetor[i]
# print('maior',maior)
# print('MENOR',menor)

# e. faça a rotação à esquerda dos elementos do vetor, por exemplo, dado o
# vetor [1,2,3,4,5] após uma rotação à esquerda o vetor ficará [2,3,4,5,1],
# após nova rotação à esquerda o vetor ficará [3,4,5,1,2].
#PRECISEI DE AJUDA NESSA AQUI
def rotacionar_esquerda(vetor,vez):
    primeiro = vetor.pop(0)   # remove o primeiro elemento
    vetor.append(primeiro)    # adiciona no final
    print( 'rotaciona',vez,'vez',vetor)
    return vetor

vtRotacionado = rotacionar_esquerda(vetor,'uma')
rotacionar_esquerda(vtRotacionado,'duas')
