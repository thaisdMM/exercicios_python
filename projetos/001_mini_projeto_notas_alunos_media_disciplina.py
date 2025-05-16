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
linha = "=-" * 50
while True:
    aluno["nome"] = input("Nome do aluno: ").strip().title()
    # aluno["Matricula"] = int(input(f"Matricula do aluno {aluno['nome']} "))
    if len(lista_alunos) == 0:
        matricula = int(input(f"Matrícula do aluno {aluno['nome']} "))
        aluno["matricula"] = matricula
        print(aluno["matricula"])

    if len(lista_alunos) != 0:
        while True:
            matricula = int(input(f"Matrícula do aluno {aluno['nome']} "))
            for valor in lista_alunos:
                print(f"valor {valor}")
                if matricula != valor["matricula"]:
                    aluno["matricula"] = matricula
                    print(f"Matricula {aluno['matricula']} cadastrada com sucesso")
                    break
                print(
                    f"Matrícula já cadastrada em outro aluno. Por favor, digite uma matricula diferente."
                )
    lista_alunos.append(aluno.copy())
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


print("\nPROGRAMA FINALIZADO!")
