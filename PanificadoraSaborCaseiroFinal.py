pedidos_pendentes=[]

def adicionarPedido(pedido):
    pedidos_pendentes.append(pedido)

def processarPedido():
    if pedidos_pendentes:
        removido = pedidos_pendentes.pop(0)
        print("Pedido processado:", removido)
    else:
        print("Nenhum pedido para processar.")

    print("Estado atual dos pedidos:", pedidos_pendentes)


def pedidosPendentes():
    Total = len(pedidos_pendentes)
    return Total

adicionarPedido([ "Café com Leite"])
adicionarPedido(["Bolo de Chocolate"])
adicionarPedido(["Pão na Chapa"]) 

processarPedido() 

print(pedidosPendentes())
