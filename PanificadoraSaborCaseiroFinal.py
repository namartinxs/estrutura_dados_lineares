import time
import questionary
pedidos_pendentes=[]

#definir prioridade
def adicionarPedidoSemPrioridade():
    pedido = input("INSIRA SEU PEDIDO: ")
    pedidos_pendentes.append([pedido]) 

def adicionarPedidoComPrioridade():
    pedido = input("INSIRA SEU PEDIDO: ")
    pedidos_pendentes.insert(0,[pedido])

def definirPrioridade():
    prioridade = questionary.select("O pedido tem prioridade?",choices=['Sim','Não']).ask()
    return prioridade == 'Sim'

#adicionar mais ou não
def adicionarPedido():
    parada = questionary.select("Mais algum pedido?",choices=['Sim','Não']).ask()
    return parada == 'Sim'

#chama todos
def realizarPedido():
    
    prioridade = definirPrioridade()
    adicao = True
    while adicao == True:
        if prioridade == True:
            adicionarPedidoComPrioridade()
            adicao = adicionarPedido()
        else:
            adicionarPedidoSemPrioridade()
            adicao = adicionarPedido()

         
    
    print('PEIDIDO(S) ADICIONADO(S):', pedidos_pendentes)


def processarPedido():
    if pedidos_pendentes:
        removido = pedidos_pendentes.pop(0)
        print("Pedido processado:", removido)
    else:
        print("Nenhum pedido para processar.")

    print("Estado atual dos pedidos:", pedidos_pendentes)

def limparPendentes():
    while pedidos_pendentes:
        time.sleep(5) 
        processarPedido()
    
def pedidosPendentes():
    Total = len(pedidos_pendentes)
    return Total

realizarPedido()
limparPendentes()
# print(pedidosPendentes())



 


