def leiaInt(msg):
    while True:
        try:
            valor_digitado = input(msg)
            valor_convertido = int(valor_digitado)
        except (ValueError, TypeError):
            print(
                f"\033[0;31mErro! '{valor_digitado}' Por favor digite um número inteiro válido!\033[m"
            )
            continue
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_convertido


def linha(tamanho=50):
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
    opcao = leiaInt("\033[32mBem vindo ao programa. Em que podemos ajudar? Digite a opção: \033[m")
    return opcao
