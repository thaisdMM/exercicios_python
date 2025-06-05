from library.interface import project_interfaces
from time import sleep

while True:
    resposta = project_interfaces.menu(
        [
            "Cadastrar alunos.",
            "Exibir alunos cadastrados.",
            "Cadastrar disciplinas.",
            "Exibir disciplinas cadastradas.",
            "Cadastrar notas por disciplina.",
            "Exibir situação de todos os alunos.",
            "Exibir a situação de um aluno específico.",
            "Excluir aluno.",
            "Trocar notas do aluno.",
            "Fim do programa.",
        ]
    )
    # queria ver se é possivel usar o tamanho da lista depois para definir o fim da resposta
    if resposta == 1:
        project_interfaces.titulo(f"{resposta}- Cadastrar alunos.")
    elif resposta == 2:
        project_interfaces.titulo(f"{resposta}- Exibir alunos cadastrados:")
    elif resposta == 3:
        project_interfaces.titulo(f"{resposta}- Cadastrar disciplinas.")
    elif resposta == 4:
        project_interfaces.titulo(f"{resposta}- Exibir disciplinas cadastradas:")
    elif resposta == 5:
        project_interfaces.titulo(f"{resposta}- Cadastrar notas por disciplina.")
    elif resposta == 6:
        project_interfaces.titulo(f"{resposta}- Exibir situação de todos os alunos.")
    elif resposta == 7:
        project_interfaces.titulo(
            f"{resposta}- Exibir a situação de um aluno específico."
        )
    elif resposta == 8:
        project_interfaces.titulo(f"{resposta}- Excluir aluno.")
    elif resposta == 9:
        project_interfaces.titulo(f"{resposta}- Trocar notas do aluno.")

    elif resposta == 10:
        project_interfaces.titulo(f"{resposta}- Fim do programa.")
        sleep(1)
        print("Volte sempre.")
        break

    else:
        print(
            f"\033[31mERRO! Opção '{resposta}' inexistente no menu. Escolha de acordo com o menu.\033[m"
        )
    sleep(1)
