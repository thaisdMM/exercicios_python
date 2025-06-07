import os


def verificar_arquivo_existe(file_path):
    file = file_path
    if os.path.exists(file_path):
        return file
    else:
        return None


# def verificar_arquivo_existe(file_path):
#     try:
#         with open(file_path, 'x') as file:
#             print(f"O arquivo foi criado em {file_path}")
#     except FileExistsError:
#         print(f"O arquivo já existe.")
#     except PermissionError:
#         print(f"Você não tem acesso para criar esse arquivo.")
