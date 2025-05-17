# Parte 1: Estrutura inicial e cadastro de alunos
# 	•	Definir a estrutura de dados principal (como organizar os alunos e suas informações).
# 	•	Fazer o cadastro dos alunos: nome e matrícula.
# Depois passamos para:
# 	•	Parte 2: Cadastro de disciplinas.
# 	•	Parte 3: Registro de notas.
# 	•	Parte 4: Relatórios e médias.
# 	•	Parte 5: Busca por aluno e refinamento final.

aluno = {}
lista_alunos = []
disciplina = {}
lista_disciplinas = [
    {"nome": "MATEMÁTICA", "codigo": 101},
    {"nome": "HISTÓRIA", "código": 102},
    {"nome": "CIÊNCIAS", "codigo": 103}
]


linha = "=-" * 50
while True:
    aluno["nome"] = input("Nome do aluno: ").strip().title()
    matricula = int(input(f"Matrícula do aluno {aluno['nome']}: "))
    while True:
        if any(matricula_existente['matricula'] == matricula for matricula_existente in lista_alunos):
            print(f"Matrícula já cadastrada. Por favor, digite outra matrícula.")
            matricula = int(input(f"Matrícula do aluno {aluno['nome']}: "))
        else:
            break
    aluno["matricula"] = matricula
    print(f"{aluno['nome']} cadastrado com sucesso com a matrícula {aluno['matricula']}")
    lista_alunos.append(aluno.copy())
    print(f"Lista de alunos cadastrados: {lista_alunos}")
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
print(f"As diciplinas já cadastradas são: ")
#while True:
for materia in lista_disciplinas:
    for key, value in materia.items():
        print(f"{key}: {value:<20} ", end="")
    print()
while True:
    print(f"dicionario de disciplina: {disciplina}")
    print(f"lista de disciplina: {lista_disciplinas}")
    cadastro_disciplina = input("Quer cadastrar alguma disciplina nova? [S/N] ").strip().upper()[0]
    if cadastro_disciplina == "N":
        print("Escolheu não cadastrar novas disciplinas.")
        break
    if cadastro_disciplina == "S":
        disciplina["nome"] = input("Qual o nome da nova disciplina que deseja cadastrar? ").strip().upper()
        disciplina["codigo"] = int(input(f"qual o código da {disciplina['nome']} "))
        print(f"dicionario de disciplina: {disciplina}")
        lista_disciplinas.append(disciplina.copy())
        disciplina.clear()
        print(f"dicionario de disciplina: {disciplina}")

    else:
        print("Resposta inválida. Digite S para sim ou N para não.")
    #break
print(linha)
print(f"As diciplinas já cadastradas são: ")
for materia in lista_disciplinas:
    for key, value in materia.items():
        print(f"{key}: {value:<20} ", end="")
    print()

print("\nPROGRAMA FINALIZADO!")
