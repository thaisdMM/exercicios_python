lista_alunos = []
lista_disciplinas = [
    {"nome": "Matematica", "codigo": 101},
    {"nome": "Historia", "codigo": 102},
    {"nome": "Ciencias", "codigo": 103},
]
linha = "=-" * 50
linha2 = "-" * 80
while True:
    aluno = {}
    aluno["nome"] = input("Nome do aluno: ").strip().title()
    while True:
        matricula = int(input(f"Matrícula do aluno {aluno['nome']}: "))
        if any(
            matricula_existente["matricula"] == matricula
            for matricula_existente in lista_alunos
        ):
            print(f"Matrícula já cadastrada. Por favor, digite outra matrícula.")
        else:
            break
    aluno["matricula"] = matricula
    print(
        f"{aluno['nome']} cadastrado com sucesso com a matrícula {aluno['matricula']}"
    )
    lista_alunos.append(aluno.copy())
    # print(f"Lista de alunos cadastrados: {lista_alunos}")
    while True:
        continuar = (
            input("Quer continuar a cadastrar alunos? [S/N] ").strip().upper()[0]
        )
        if continuar in "SN":
            break
        print("Escolha inválida. Digite S para sim ou N para não.")
    if continuar == "N":
        print("Não quer continuar a cadastrar mais alunos.")
        break
# print(f"Lista de alunos cadastrados: {lista_alunos}")
print(linha)
print("Os alunos cadastrados até o momento são:")
print()
for valor in lista_alunos:
    for key, value in valor.items():
        print(f"{key} = {value:<40} ", end="")
    print()
print(linha)
print(f"As disciplinas obrigatórias já cadastradas são: ")
print()
for materia in lista_disciplinas:
    for key, value in materia.items():
        print(f"{key}: {value:<20} ", end="")
    print()
print(linha)
while True:
    disciplina = {}
    # print(f"dicionario de disciplina: {disciplina}")
    # print(f"lista de disciplina: {lista_disciplinas}")
    cadastro_disciplina = (
        input("Quer cadastrar alguma disciplina nova? [S/N] ").strip().title()[0]
    )
    if cadastro_disciplina == "N":
        print("Escolheu não cadastrar novas disciplinas.")
        break
    if cadastro_disciplina == "S":
        while True:
            nova_disciplina = (
                input("Qual o nome da nova disciplina que deseja cadastrar? ")
                .strip()
                .title()
            )
            if any(
                disciplina_existente["nome"] == nova_disciplina
                for disciplina_existente in lista_disciplinas
            ):
                print(f"A disciplina {nova_disciplina} já está cadastrada.")
            else:
                break
        disciplina["nome"] = nova_disciplina
        while True:
            codigo_nova_disciplina = int(
                input(f"Qual o código da {disciplina['nome']}? ")
            )
            if any(
                codigo_existente["codigo"] == codigo_nova_disciplina
                for codigo_existente in lista_disciplinas
            ):
                print(
                    f"O código {codigo_nova_disciplina} já está associado a outra disciplina. Digite outro código!"
                )
            else:
                break
        disciplina["codigo"] = codigo_nova_disciplina
        # print(f"dicionario de disciplina: {disciplina}")
        lista_disciplinas.append(disciplina.copy())
        disciplina.clear()
        # print(f"dicionario de disciplina: {disciplina}")
    else:
        print("Resposta inválida. Digite S para sim ou N para não.")
print(linha)
print(f"As disciplinas já cadastradas são: ")
print()
for materia in lista_disciplinas:
    for key, value in materia.items():
        print(f"{key}: {value:<20} ", end="")
    print()
print(linha)
for aluno in lista_alunos:
    disciplina_alunos = []
    for disciplina in lista_disciplinas:
        disciplina_alunos.append(
            {
                "nome": disciplina["nome"],
                "codigo": disciplina["codigo"],
                "notas": [],
            }
        )
    aluno["disciplina"] = disciplina_alunos[:]
    # print(f"dicionario {aluno}")
for aluno in lista_alunos:
    print(f"Aluno(a): {aluno['nome']}")
    for materia in aluno["disciplina"]:
        nota1 = float(input(f"Digite a 1ª nota tirada em {materia['nome']} "))
        nota2 = float(input(f"Digite a 2ª nota tirada em {materia['nome']} "))
        materia["notas"] = [nota1, nota2]
        materia["media"] = (nota1 + nota2) / 2
        if materia["media"] >= 7:
            materia["situacao"] = "Aprovado"
        elif materia["media"] > 5:
            materia["situacao"] = "Recuperação"
        else:
            materia["situacao"] = "Reprovado"
        # print(f"Materia: {materia}")
    print(linha2)
print(linha)
print("O relatório geral de todos os alunos cadastrados é o seguinte:")
print(linha)
for aluno in lista_alunos:
    print(f"{aluno['nome']:^60}")
    print(f"Matrícula do aluno: {aluno['matricula']}")
    print("As disciplinas cursadas são: ")
    for materia in aluno["disciplina"]:
        print(f"{materia}")
    print(linha2)
print(linha)
while True:
    busca = int(
        input(
            "Digite a matrícula do aluno que deseja saber os dados? [Digite 999 se quiser parar o programa] "
        )
    )
    if busca == 999:
        print("Finalizando programa.")
        break
    aluno_existe = False
    for aluno in lista_alunos:
        if busca == aluno["matricula"]:
            aluno_existe = True
            print(f"{aluno['nome']:^60}")
            print(f"Matrícula do aluno: {aluno['matricula']}")
            print("As disciplinas cursadas são: ")
            for materia in aluno["disciplina"]:
                print(f"{materia}")
            print(linha)
            break
    if not aluno_existe:
        print("Número de matrícula inexistente. Tente novamente.")
print("\nPROGRAMA FINALIZADO!")
