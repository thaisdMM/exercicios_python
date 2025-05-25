def titulo(msg):
    tamanho = len(msg) + 4
    print("*" * tamanho)
    print(f"  {msg}")
    print("*" * tamanho)
    return


def cadastro_alunos(lista_alunos, nome_aluno, matricula_aluno):
    aluno = {"nome": nome_aluno, "matricula": matricula_aluno}
    lista_alunos.append(aluno.copy())
    print(
        f"{nome_aluno}: foi cadastrado(a) com sucesso com a matrícula {matricula_aluno}!"
    )
    print("=-" * 50)
    return


def mostrar_alunos(lista_alunos):
    for aluno in lista_alunos:
        for key, value in aluno.items():
            print(f"{key} = {value:<20}", end="")
        print()
    print("=-" * 50)
    return


def cadastro_disciplinas(lista_disciplinas, nome_disciplina, codigo_disciplina):
    disciplina = {"nome": nome_disciplina, "codigo": codigo_disciplina}
    lista_disciplinas.append(disciplina.copy())
    print(
        f"Disciplina: {nome_disciplina} cadastrada com sucesso com o código {codigo_disciplina}"
    )
    disciplina.clear()
    print("=-" * 50)
    return


def mostrar_disciplinas(lista_disciplinas):
    print("Lista de disciplinas:")
    print()
    for disciplina in lista_disciplinas:
        for key, value in disciplina.items():
            print(f"{key} = {value:<20}", end="")
        print()
    print("=-" * 50)


def continuar():
    while True:
        continuar = (
            input("Deseja continuar a cadastrar alunos? [S/N] ").strip().upper()[0]
        )
        if continuar not in "NS":
            print("Resposta inválida. Responda S para continuar ou N para parar.")
        if continuar == "N":
            break


# PROGRAMA PRINCIPAL:
lista_alunos = []
lista_disciplinas = []
linha1 = "-" * 70

while True:
    print(
        """
    MENU PROGRAMA DE ALUNOS E DISCIPLINAS

    1- Cadastrar alunos.
    2- Exibir alunos cadastrados.
    3- Cadastrar disciplinas.
    4- Exibir disciplinas cadastradas.
    5- Cadastrar notas por disciplina.
    6- Exibir situação de todos os alunos.
    7- Exibir a situação de um aluno específico.
    8- Excluir aluno.
    9- Trocar notas do aluno.
    10- Fim do programa.
    """
    )
    while True:
        resposta = input(
            "Bem vindo ao programa. Em que podemos ajudar? Digite a opção: "
        ).strip()
        if not resposta.isnumeric():
            print("Resposta inválida! Digite de acordo com o menu.")
        else:
            resposta = int(resposta)
            if 0 < resposta <= 10:
                break
            else:
                print("Resposta inválida! Digite de acordo com o menu.")
        print(linha1)

    if resposta == 1:
        titulo("1- Cadastrar alunos.")
        nome_aluno = input("Nome do aluno: ").strip().title()
        while True:
            matricula_aluno = int(input(f"Matrícula do aluno {nome_aluno}: "))
            # fazer uma validação se não for número.
            if any(
                matricula_existente["matricula"] == matricula_aluno
                for matricula_existente in lista_alunos
            ):
                print(
                    f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Por favor, digite outro número de matrícula."
                )
                print(linha1)
            else:
                break
        print(linha1)
        cadastro_alunos(lista_alunos, nome_aluno, matricula_aluno)

    if resposta == 2:
        titulo("2- Exibir alunos cadastrados:")
        mostrar_alunos(lista_alunos)

    if resposta == 3:
        titulo("2- Cadastrar disciplinas.")
        while True:
            nome_disciplina = input("Nome da disciplina: ").strip().title()
            if any(
                disciplina_existente["nome"] == nome_disciplina
                for disciplina_existente in lista_disciplinas
            ):
                print(
                    f"A disciplina {nome_disciplina} já está cadastrada. Por favor digite outra disciplina."
                )
                print(linha1)
            else:
                break
        while True:
            # quero limitar o codigo a apenas 3 digitos
            # quero importar depois a função leiaInt() que eu fiz, para aceitar só valores numéricos
            codigo_disciplina = int(input(f"Código da disciplina {nome_disciplina}: "))
            if any(
                codigo_existente["codigo"] == codigo_disciplina
                for codigo_existente in lista_disciplinas
            ):
                print(
                    f"O código {codigo_disciplina} já está cadastrada em outra disciplina. Por favor digite outro código."
                )
                print(linha1)
            else:
                break
        cadastro_disciplinas(lista_disciplinas, nome_disciplina, codigo_disciplina)

    if resposta == 4:
        titulo("4- Exibir disciplinas cadastradas")
        mostrar_disciplinas(lista_disciplinas)

    if resposta == 10:
        print("Volte sempre.")
        print(linha1)
        break


print(lista_alunos)
print(lista_disciplinas)
print("\nPrograma finalizado!")
