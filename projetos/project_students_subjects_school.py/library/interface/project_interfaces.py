def linha(tamanho = 50):
    return "-" * tamanho


def titulo(msg):
    tamanho = len(msg) + 4
    print("*" * tamanho)
    print(f"  {msg}")
    print("*" * tamanho)
    return


def menu(lista):
    titulo("MENU DE SISTEMA DE ALUNOS E DISCIPLINAS")
    contador = 1
    for item in lista:
        print(f"\033[33m{contador:2}\033[m - \033[34m{item}\033[m")
        contador += 1
    print(linha())