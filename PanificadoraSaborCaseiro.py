estoque_do_dia = ["Pão Francês", "Bolo de Cenoura", "Pão de Queijo", "Sonho", "Bolo de Cenoura"]

'''1. Adicione "Croissant" ao final da estoque_do_dia.'''
estoque_do_dia.append("Croissant")

'''2. Adicione "Pão Doce" no início da estoque_do_dia.'''
estoque_do_dia.insert(0,"Pão Doce")

'''3. Uh oh! Um cliente muito faminto comprou o último "Sonho". Remova o "Sonho" da lista.'''
estoque_do_dia.remove("Sonho")

'''4. Mostre como o estoque_do_dia se parece agora.'''
# print(estoque_do_dia)

'''2. Contando as Delícias: Quantos de Cada?
O gerente quer saber rapidamente quantos "Bolo de Cenoura" foram feitos hoje.
• Pense nisso: Existe uma maneira rápida e fácil de contar ocorrências de um item em uma
lista? Se você tentasse contar um item que não existe, o que aconteceria?
• Sua vez de Codificar:
1. Conte quantas vezes "Bolo de Cenoura" aparece na estoque_do_dia (use a lista após
as modificações do Exercício 1).'''
#print(estoque_do_dia.count("Bolo de Cenoura"))

'''2. Tente contar "Brigadeiro" (um item que não está na lista). O que o Python retorna? Isso
é um erro ou algo útil?'''
#print(estoque_do_dia.count("Morango do amor"))


'''3. Arrume a Prateleira! Classificando o Estoque
Para facilitar a vida dos padeiros, a lista precisa ser organizada em ordem alfabética.
• Pense nisso: Qual método de lista você usaria para classificar os itens? O método
modifica a lista original ou cria uma nova?
• Sua vez de Codificar (com Lápis e Papel, se quiser!):
1. Ordene o estoque_do_dia em ordem alfabética.
2. Imprima a lista ordenada.'''

#metodo do python, retorna uma nova lista mantem a lista original intacta
lista_ordenada = sorted(estoque_do_dia)
# print(lista_ordenada) 

#metodo para listas, altera lista original
#print('antes',estoque_do_dia)
# estoque_do_dia.sort() 
# print('depois',estoque_do_dia) 

'''3. O cliente VIP gosta dos itens mais caros primeiro. Supondo que "Sonho" fosse o mais
caro e "Pão Francês" o mais barato, como você poderia inverter a ordem da lista já
classificada, para que o "Sonho" (se estivesse lá) aparecesse primeiro? (Não se preocupe
em adicionar o sonho de volta agora, apenas pense na operação).
• Pausa para Pensar: Qual é a diferença entre list.sort() e sorted(list)? Quando você usaria
um em vez do outro? Escreva uma pequena nota sobre isso em seu caderno.''' 

estoque_do_dia.reverse()

#print("Estoque invertido (VIP):", estoque_do_dia)
# 4. Estoque Duplicado? Cuidado com as Referências!
# Um padeiro júnior, empolgado, criou uma "lista de verificação" baseada no seu
# estoque_do_dia original, mas sem querer, ele modificou o seu estoque principal!
# • Código Inicial (para este exercício):
# • Pense nisso: O que você espera ver se imprimir estoque_principal depois que
# lista_de_verificacao foi modificada? Por que isso acontece? Como o padeiro júnior poderia
# ter feito uma cópia segura da lista para evitar modificar a original?
# • Sua vez de Codificar:
# 1. Execute o código acima.
# 2. Imprima estoque_principal e lista_de_verificacao. O que você observa?
# 3. Corrija a linha onde lista_de_verificacao é criada para que ela seja uma cópia
# independente de estoque_principal.
# 4. Execute novamente e imprima as duas listas para confirmar que a modificação em
# lista_de_verificacao não afeta estoque_principal.

estoque_do_dia1 = ["Pão Francês", "Bolo de Cenoura", "Pão de Queijo", "Sonho", "Bolo de Cenoura"]
list_verificacao = estoque_do_dia1 #nao é uma nova lista apenas nova referencia
list_verificacao.remove("Sonho") 
# print('estoque',estoque_do_dia1)
# print('verificacao',list_verificacao)
#removeu sonho das duas 

estoque_principal = ["Pão Francês", "Bolo de Cenoura", "Pão de Queijo", "Sonho", "Bolo de Cenoura"]
'''correcao 
# Forma 1: usando slicing
lista_de_verificacao = estoque_principal[:]

# Forma 2: usando copy()
# lista_de_verificacao = estoque_principal.copy()
# '''

lista_verificacao = estoque_principal.copy()
lista_verificacao.remove("Sonho")
print('estoque',estoque_principal)
print('remove',lista_verificacao)

#corrige o endereçamento