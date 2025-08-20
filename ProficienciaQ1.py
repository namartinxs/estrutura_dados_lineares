import random
linhas = int(input("Quantas linhas você deseja?"))
colunas = int(input("Quantas colunas você deseja?") )

aleatorias = []
for i in range(5):
    while True:
        letra = input(f"insira sua {i+1}º letra ")
        #type não rola, input sempre string
        if(letra.isalpha()):
            aleatorias.append(letra)
            break
        else:
         print('apenas letras por favor!')
   


matriz = []
for i in range(linhas):
   linha = []
   for j in range(colunas):
        #escolha aleatoria dentro de um universo
        letra = random.choice(aleatorias)
        linha.append(letra)
   matriz.append(linha)
      
for linha in matriz:
    print(linha)