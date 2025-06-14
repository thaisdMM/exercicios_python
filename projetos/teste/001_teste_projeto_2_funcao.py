# # def associacao_disciplinas_alunos(lista_alunos, lista_disciplinas):
# #     for aluno in lista_alunos:
# #         # print(f"ALUNO NO INICIO {aluno}")
# #         if not aluno["disciplina"]:
# #             aluno["disciplina"] = []
# #         for disciplina in lista_disciplinas:
# #             # print(f"DISCIPLINA NO RANGE DA LISTA DE DISCIPLINA {disciplina}")
# #             if any(
# #                 codigo_existente["codigo"] == disciplina["codigo"]
# #                 for codigo_existente in aluno["disciplina"]
# #             ):
# #                 continue
# #             else:
# #                 aluno["disciplina"].append(
# #                     {
# #                         "nome": disciplina["nome"],
# #                         "codigo": disciplina["codigo"],
# #                         "notas": [],
# #                     }
# #                 )
# #         # print(f"ALUNO NO FIM: {aluno}")


# # alunos = [
# #     {"nome": "marcelo", "matricula": 123, "disciplina": []},
# #     {"nome": "marcia", "matricula": 321, "disciplina": []},
# # ]
# # disciplina = [
# #     {"nome": "Portugues", "codigo": 105},
# #     {"nome": "matemática", "codigo": 103},
# # ]

# # print(f"FUNÇÃO 1 VEZ: ")
# # associacao_disciplinas_alunos(alunos, disciplina)
# # print()
# # print("2 vez")
# # associacao_disciplinas_alunos(alunos, disciplina)


# def continuar():
#     resposta = None
#     while resposta == None:
#         try:
#             continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
#             if continuar not in "NS":
#                 print("Resposta inválida. Responda S para continuar ou N para parar.")
#                 resposta = None
#             if continuar == "N":
#                 resposta = False
#             if continuar == "S":
#                 resposta = True
#         except (ValueError, TypeError, IndexError, KeyboardInterrupt):
#             print("Resposta inválida. Responda S para continuar ou N para parar.")
#             resposta = None
#     return resposta


# while True:
#     decisao = continuar()
#     if not decisao:
#         break
#     if decisao:
#         print("continuar")

import os

caminho1 = "/home/user/arquivo.txt"
caminho2 = "files_create/cadastro_alunos_matricula.json"

print(os.path.isabs(caminho1))  # True
print(os.path.isabs(caminho2))  # False


def absolute_path(file_path):
    # Caminho absoluto da pasta onde este arquivo está localizado
    PASTA_BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # Se file_path já for um caminho absoluto, retorna ele mesmo
    if os.path.isabs(file_path):
        print("absoluto")
        return file_path
    else:
        # Caso contrário, junta o caminho da pasta base com file_path
        # para formar o caminho absoluto completo até o arquivo
        CAMINHO_ARQUIVO = os.path.join(PASTA_BASE, file_path)
        print("relativo")
        return CAMINHO_ARQUIVO


path = absolute_path(caminho1)
print(path)

path = absolute_path(caminho2)
print(path)
