import questionary
#pip install questionary
# pip install prompt_toolkit==3.0.20

def menu():
    resposta = questionary.select(
        "O pedido é prioritário?",
        choices=[
            "Sim",
            "Não"
        ]
    ).ask()

    return resposta == "Sim"
# Uso:
prioridade = menu()
print("Prioridade:", prioridade)
