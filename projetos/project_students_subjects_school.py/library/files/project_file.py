import os
import json


def verificar_arquivo_existe(file_path):
    file = file_path
    if os.path.exists(file_path):
        return file
    else:
        return None


def criar_arquivo(file_path):
    data = []
    try:
        with open(file_path, "x") as file:
            pass
    except FileExistsError:
        print(f"O arquivo já existe")
    except PermissionError:
        print(f"Você não tem permissão para criar esse arquivo.")


def subscrever_arquivo(file_paht, data):
    try:
        with open(file_paht, "w") as file:
            json.dump(data, file, indent=4)
            return file
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except PermissionError:
        return "Você não tem permissão para criar esse arquivo."


def append_arquivo(file_path, data):
    try:
        with open(file_path, "a") as append_file:
            json.dump(data, append_file, indent=4)
            return append_file
    except PermissionError:
        return "Você não tem permissão para criar esse arquivo."


# def verificar_arquivo_existe(file_path):
#     try:
#         with open(file_path, 'x') as file:
#             print(f"O arquivo foi criado em {file_path}")
#     except FileExistsError:
#         print(f"O arquivo já existe.")
#     except PermissionError:
#         print(f"Você não tem acesso para criar esse arquivo.")
