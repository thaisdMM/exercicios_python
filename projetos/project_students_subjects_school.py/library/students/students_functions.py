from library.subjects import subjects_functions


def cadastro_alunos(lista_alunos, nome_aluno, matricula_aluno):
    try:
        aluno = {"nome": nome_aluno, "matricula": matricula_aluno, "disciplina": []}
    except (ValueError, TypeError):
        print(f"Os dados inseridos apresentam erros.")
    try:
        lista_alunos.append(aluno.copy())
        # subjects_functions.associacao_disciplinas_alunos(lista_alunos, lista_disciplinas)
    except FileNotFoundError:
        print("Não foi possivel anexar a lista ao dicionário. O arquivo não foi encontrado.")
    else:
        print(
            f"{nome_aluno}: foi cadastrado(a) com sucesso com a matrícula {matricula_aluno}!"
        )
    print("=-" * 50)
    return


def mostrar_alunos(lista_alunos):
    print("LISTA DE ALUNOS:")
    print()
    if len(lista_alunos) <= 0:
        print("Ainda não existem alunos cadastrados.")
    else:
        for aluno in lista_alunos:
            print(f"{aluno['nome']:<5} = matrícula {aluno['matricula']}", end="")
            print()
            print("-" * 60)
    print("=-" * 50)


def buscar_aluno(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def exibir_dados_alunos(lista_alunos, matricula):
    aluno = buscar_aluno(lista_alunos, matricula)
    if aluno == None:
        print(
            "Não há aluno com a matrícula pesquisada. Verifique a matrícula do aluno que quer exibir os dados."
        )
    else:
        for key, value in aluno.items():
            print(f"{key:<10} = {value}")
    print("=-" * 50)


def excluir_aluno(lista, aluno):
    if aluno is None:
        return False
    else:
        lista.remove(aluno)
        return True
