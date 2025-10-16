from Fila import Fila

if __name__ == '__main__':
    fila = Fila()
    fila.enfilerar(10)
    fila.enfilerar(20)
    fila.enfilerar(30)

    print("Conteúdo da fila:")
    fila.mostrar_fila()

    print("\nDesenfileirando um elemento...")
    removido = fila.desenfilerar()
    print(f"Elemento removido: {removido}")

    print("\nConteúdo da fila após desenfileirar:")
    fila.mostrar_fila()

    print(f"\nTamanho atual da fila: {fila.getTamanho()}")
