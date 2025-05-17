# Parte 1: Estrutura inicial e cadastro de alunos
# 	•	Definir a estrutura de dados principal (como organizar os alunos e suas informações).
# 	•	Fazer o cadastro dos alunos: nome e matrícula.
# Depois passamos para:
# 	•	Parte 2: Cadastro de disciplinas.
# 	•	Parte 3: Registro de notas.
# 	•	Parte 4: Relatórios e médias.
# 	•	Parte 5: Busca por aluno e refinamento final.


lista_alunos = []
lista_disciplinas = [
    {"nome": "Matematica", "codigo": 101},
    {"nome": "Historia", "codigo": 102},
    {"nome": "Ciencias", "codigo": 103},
]

lista_notas = []
linha = "=-" * 50
linha2 = "-" * 70
while True:
    aluno = {}
    aluno["nome"] = input("Nome do aluno: ").strip().title()
    matricula = int(input(f"Matrícula do aluno {aluno['nome']}: "))
    while True:
        if any(
            matricula_existente["matricula"] == matricula
            for matricula_existente in lista_alunos
        ):
            print(f"Matrícula já cadastrada. Por favor, digite outra matrícula.")
            matricula = int(input(f"Matrícula do aluno {aluno['nome']}: "))
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
        print("Não quer continuar o cadastro.")
        break
# print(f"Lista de alunos cadastrados: {lista_alunos}")
print(linha)
for posicao, valor in enumerate(lista_alunos):
    for key, value in valor.items():
        print(f"{key} = {value:<40} ", end="")
    print()
print(linha)
print(f"As disciplinas já cadastradas são: ")
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
        nova_disciplina = (
            input("Qual o nome da nova disciplina que deseja cadastrar? ")
            .strip()
            .title()
        )
        while True:
            if any(
                disciplina_existente["nome"] == nova_disciplina
                for disciplina_existente in lista_disciplinas
            ):
                print(f"A disciplina {nova_disciplina} já está cadastrada.")
                nova_disciplina = (
                    input("Qual o nome da nova disciplina que deseja cadastrar? ")
                    .strip()
                    .title()
                )
            else:
                break
        disciplina["nome"] = nova_disciplina
        codigo_nova_disciplina = int(input(f"Qual o código da {disciplina['nome']}? "))
        while True:
            if any(
                codigo_existente["codigo"] == codigo_nova_disciplina
                for codigo_existente in lista_disciplinas
            ):
                print(
                    f"O código {codigo_nova_disciplina} já está associado a outra disciplina. Digite outro código!"
                )
                codigo_nova_disciplina = int(
                    input(f"Qual o código da {disciplina['nome']}? ")
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
    # break
print(linha)
print(f"As disciplinas já cadastradas são: ")
for materia in lista_disciplinas:
    for key, value in materia.items():
        print(f"{key}: {value:<20} ", end="")
    print()
print(linha)
for aluno in lista_alunos:
    disciplina_alunos = []
    for disciplina in lista_disciplinas:
        disciplina_alunos.append(
            {"nome": disciplina["nome"], "codigo": disciplina["codigo"], "notas": []}
        )
    aluno["disciplina"] = disciplina_alunos[:]
    # print(f"dicionario {aluno}")
# lista_alunos.append(aluno.copy())
for aluno in lista_alunos:
    for key, value in aluno.items():
        print(f"{key}: {str(value):<10} ")
    # print()
    print(linha2)


for aluno in lista_alunos:
    print(f"Aluno(a): {aluno['nome']}")
    for materia in aluno["disciplina"]:
        nota1 = float(input(f"Digite a 1ª nota tirada em {materia['nome']} "))
        nota2 = float(input(f"Digite a 2ª nota tirada em {materia['nome']} "))
        materia["notas"] = nota1, nota2
        print(f"Materia: {materia}")
    print(linha2)
print(linha)
for aluno in lista_alunos:
    for key, value in aluno.items():
        print(f"{key}: {str(value):<10}")
    print()

# for valor in lista_alunos:
#     print(f"Valor em lista de alunos {valor}")
#     for key, value in valor.items():
#         key["disciplina"] = lista_disciplinas[:]
#         print(f"novo Valor em lista de alunos {valor}")

# print(lista_alunos)

print("\nPROGRAMA FINALIZADO!")
