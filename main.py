from time import sleep
import funcoes

arq = "banco.txt"

funcoes.verifica_banco(arq)

while True:
    escolha = funcoes.menu(
        "Adicionar Tarefas",
        "Listar Tarefas",
        "Marcar Tarefas Concluidas",
        "Remover Tarefas",
        "Sair",
    )

    if escolha == 1:
        funcoes.cabecalho("Adicionar Tarefas")

        while True:
            descricao = (
                input("Qual tarefa você deseja adicionar a lista?: ")
                .strip()
                .capitalize()
            )
            if descricao == "":
                print("Erro, a tarefa não pode eestar vazia!")
            else:
                break

        funcoes.adicionar_tarefas(arq, descricao)

    if escolha == 2:
        funcoes.cabecalho("Lista de Tarefas")
        tarefas = funcoes.carregar_tarefas(arq)
        contador = 1

        if tarefas:
            for i, v in enumerate(tarefas, start=1):
                if v["concluida"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(f"{i} - {status} - {v['descricao']}")
        else:
            print("Lista de tarefas vazia!")

        print("")
        print("")
        sleep(2)

    if escolha == 3:
        funcoes.cabecalho("Marcar Tarefas Concluidas")
        tarefas = funcoes.carregar_tarefas(arq)

        if tarefas:
            for i, v in enumerate(tarefas, start=1):
                if v["concluida"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(f"{i} - {status} - {v['descricao']}")

            while True:
                index = funcoes.leia_int(
                    "Qual o número da tarefa que você deseja marcar como concluida?: "
                )
                if 0 < index <= len(tarefas):
                    break
                else:
                    print("Erro, essa tarefa não existe")

            funcoes.marcar_concluida(arq, index)
        else:
            print("Lista de tarefas vazia!")

        print("")
        print("")
        sleep(2)

    if escolha == 4:
        funcoes.cabecalho("Remover Tarefas")
        tarefas = funcoes.carregar_tarefas(arq)

        if tarefas:
            for i, v in enumerate(tarefas, start=1):
                if v["concluida"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(f"{i} - {status} - {v['descricao']}")

            while True:
                index = funcoes.leia_int(
                    "Qual o número da tarefa que você deseja remover?: "
                )
                if 0 < index <= len(tarefas):
                    break
                else:
                    print("Erro, essa tarefa não existe")

            funcoes.remover_tarefas(arq, index)

        else:
            print("Adicione tarefas a lista antes!")

        print("Tarefa removida com sucesso!")
        print("")
        print("")
        sleep(2)

    if escolha == 5:
        funcoes.cabecalho("Saindo")
        sleep(2)
        break
