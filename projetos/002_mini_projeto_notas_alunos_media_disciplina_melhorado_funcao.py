def titulo(msg):
    tamanho = len(msg) + 4
    print("*" * tamanho)
    print(f"  {msg}")
    print("*" * tamanho)
    return


def cadastro_alunos(lista_alunos, nome_aluno, matricula_aluno):
    aluno = {"nome": nome_aluno, "matricula": matricula_aluno, "disciplina": []}
    lista_alunos.append(aluno.copy())
    associacao_disciplinas_alunos(lista_alunos, lista_disciplinas)
    print(
        f"{nome_aluno}: foi cadastrado(a) com sucesso com a matrícula {matricula_aluno}!"
    )
    print("=-" * 50)
    return


def mostrar_alunos(lista_alunos):
    print("LISTA DE ALUNOS:")
    print()
    for aluno in lista_alunos:
        print(f"{aluno['nome']:<10} = matrícula {aluno['matricula']}", end="")
        #     for key, value in aluno.items():
        #         print(f"{key:<5} = {value}", end="  ")
        print()
        print("-" * 60)
    print("=-" * 50)


def cadastro_disciplinas(lista_disciplinas, nome_disciplina, codigo_disciplina):
    disciplina = {"nome": nome_disciplina, "codigo": codigo_disciplina}
    lista_disciplinas.append(disciplina.copy())
    associacao_disciplinas_alunos(lista_alunos, [disciplina])
    print(
        f"Disciplina: {nome_disciplina} cadastrada com sucesso com o código {codigo_disciplina}"
    )
    print("=-" * 50)
    return


def mostrar_disciplinas(lista_disciplinas):
    print("LISTA DE DISCIPLINAS:")
    print()
    for disciplina in lista_disciplinas:
        for key, value in disciplina.items():
            print(f"{key:<5} = {value}", end="  ")
        print()
    print("=-" * 50)


def associacao_disciplinas_alunos(lista_alunos, lista_disciplinas):
    for aluno in lista_alunos:
        for disciplina in lista_disciplinas:
            if any(
                codigo_existente["codigo"] == disciplina["codigo"]
                for codigo_existente in aluno["disciplina"]
            ):
                continue
            else:
                aluno["disciplina"].append(
                    {
                        "nome": disciplina["nome"],
                        "codigo": disciplina["codigo"],
                        "notas": [],
                        "media": 0.0,
                        "situacao": False,
                    }
                )


def cadastro_notas(aluno, codigo_disciplina, nota1, nota2):
    for valor in aluno["disciplina"]:
        if valor["codigo"] == codigo_disciplina:
            valor["notas"] = [nota1, nota2]
            print(
                f"As notas: {valor['notas']} foram cadastras com sucesso para o aluno(a) {aluno['nome']}  em {valor['nome']}"
            )
            valor["media"] = sum(valor["notas"]) / len(valor["notas"])
    print("=-" * 50)
    return


def situacao_aluno(aluno):
    for valor in aluno["disciplina"]:
        situacao = ""
        if len(valor["notas"]) <= 0:
            situacao = "INDEFINIDA"
        else:
            if valor["media"] >= 7:
                situacao = "APROVADO"
            elif valor["media"] >= 5:
                situacao = "RECUPERAÇÃO"
            else:
                situacao = "REPROVADO"
        valor["situacao"] = situacao

        print(f"A situação do {aluno['nome']} é: ")
        print(f"{valor['nome']} = {valor['situacao']}")
        print()
    print("-" * 50)
    return


def buscar_aluno(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

def exibir_dados_alunos(matricula):
    aluno = buscar_aluno(lista_alunos, matricula)
    for key, value in aluno.items():
        print(f"{key:<10} = {value}")

    # for aluno in lista_alunos:
    #     if any(matricula_existente['matricula'] == matricula_aluno for matricula_existente in lista_alunos):
    #         print(aluno)
    #         for key, value in aluno.items():
    #             print(f"{key:<10} = {value}")
    #         break
    #         # for key, value in aluno.items():
    #         #     print(f"{key:<10} = {value}")
    #     else:
    #         print("Não há aluno com a matrícula pesquisa. Verifique a matrícula do aluno.")
    # return


def continuar():
    while True:
        continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
        if continuar not in "NS":
            print("Resposta inválida. Responda S para continuar ou N para parar.")
        if continuar == "N":
            break
    return


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
        titulo("4- Exibir disciplinas cadastradas:")
        mostrar_disciplinas(lista_disciplinas)

    if resposta == 5:
        titulo("5- Cadastrar notas por disciplina:")
        mostrar_alunos(lista_alunos)
        mostrar_disciplinas(lista_disciplinas)
        if len(lista_disciplinas) <= 0 or len(lista_alunos) <= 0:
            print(
                "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno."
            )
        else:
            while True:
                codigo_disciplina = int(
                    input(
                        "Digite o código da disciplina que deseja cadastrar as notas: "
                    )
                )
                if any(
                    codigo_existente["codigo"] == codigo_disciplina
                    for codigo_existente in lista_disciplinas
                ):
                    break
                else:
                    print(
                        "Código de disciplina inexistente. Por favor digite o código correto."
                    )
            for aluno in lista_alunos:
                for disciplina in aluno["disciplina"]:
                    if disciplina["codigo"] == codigo_disciplina:
                        # if any(notas_existente['notas'] >= len(disciplina['notas']) for notas_existente in aluno['disciplina']):
                        if len(disciplina["notas"]) > 0:
                            continue
                        else:

                            print(
                                f"Notas de {aluno['nome']} na disciplina {disciplina['nome']}:"
                            )
                            nota1 = float(input("1ª nota: "))
                            nota2 = float(input("2ª nota: "))
                            print(linha1)
                            cadastro_notas(aluno, codigo_disciplina, nota1, nota2)
                            print(linha1)
                            continue

    if resposta == 6:
        titulo("6- Exibir situação de todos os alunos:")
        if len(lista_alunos) <= 0 or len(lista_disciplinas) <= 0:
            print(
                "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno e notas."
            )
        else:
            for aluno in lista_alunos:
                situacao_aluno(aluno)

    if resposta == 7:
        titulo("7- Exibir a dados de um aluno específico:")
        mostrar_alunos(lista_alunos)
        matricula_pesquisada = int(
            input("Digite a matrícula do aluno que deseja ver os dados: ")
        )
        buscar_aluno(lista_alunos, matricula_pesquisada)
        if buscar_aluno(lista_alunos, matricula_pesquisada) == None:
            print("Não há aluno com a matrícula pesquisa. Verifique a matrícula do aluno.")
        else:
            exibir_dados_alunos(matricula_pesquisada)
        
        # for aluno in lista_alunos:
        #     if any(
        #         matricula_existente["matricula"] == matricula_pesquisada
        #         for matricula_existente in lista_alunos
        #     ):
        #         exibir_dados_alunos(aluno['matricula'], matricula_pesquisada)
        #         break
            
    if resposta == 10:
        print("Volte sempre.")
        print(linha1)
        break


print(lista_alunos)
print(lista_disciplinas)
print("\nPrograma finalizado!")
