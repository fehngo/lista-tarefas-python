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
        resposta = (
            input("Qual tarefa você deseja adicionar a lista?: ").strip().capitalize()
        )
        funcoes.adicionar_tarefas(arq, resposta)
        print("")
        print("")
        sleep(2)

    if escolha == 2:
        funcoes.cabecalho("Lista de Tarefas")
        tarefas = funcoes.ler_arquivo(arq)
        if tarefas:
            for i, linha in enumerate(tarefas):
                descricao, sit = linha.strip().split(";")
                if sit == "True":
                    print(f"{i+1} - [x] {descricao}")
                else:
                    print(f"{i+1} - [ ] {descricao}")
        else:
            print("Lista de tarefas vazia!")
        print("")
        print("")
        sleep(2)

    if escolha == 3:
        funcoes.cabecalho("Marcar Tarefas Concluidas")

        tarefas = funcoes.ler_arquivo(arq)
        if tarefas:
            for i, linha in enumerate(tarefas):
                descricao, sit = linha.strip().split(";")
                if sit == "True":
                    print(f"{i+1} - [x] {descricao}")
                else:
                    print(f"{i+1} - [ ] {descricao}")
        else:
            print("Lista de tarefas vazia!")
        print("")

        index = funcoes.leia_int(
            "Qual o número da tarefa que você deseja marcar como concluida?: "
        )
        texto = funcoes.ler_linhas(arq)
        nova_lista = list()

        if texto:
            for i, linha in enumerate(texto):
                if i + 1 == index:
                    descricao, sit = linha.strip().split(";")
                    nova_lista.insert(0, f"{descricao};{True}")
                else:
                    nova_lista.append(linha.strip())

            funcoes.zerar_lista(arq)
            for valor in nova_lista:
                funcoes.marcar(arq, valor)

        else:
            print("Adicione tarefas a lista antes!")

        print("Tarefa marcada com sucesso!")
        print("")
        print("")
        sleep(2)

    if escolha == 4:
        funcoes.cabecalho("Remover Terefas")

        tarefas = funcoes.ler_arquivo(arq)
        if tarefas:
            for i, linha in enumerate(tarefas):
                descricao, sit = linha.strip().split(";")
                if sit == "True":
                    print(f"{i+1} - [x] {descricao}")
                else:
                    print(f"{i+1} - [ ] {descricao}")
        else:
            print("Lista de tarefas vazia!")
        print("")

        index = funcoes.leia_int("Qual o número da tarefa que você deseja remover?: ")
        texto = funcoes.ler_linhas(arq)
        nova_lista = list()

        if texto:
            for i, linha in enumerate(texto):
                if i + 1 == index:
                    pass
                else:
                    nova_lista.append(linha.strip())

            funcoes.zerar_lista(arq)
            for valor in nova_lista:
                funcoes.marcar(arq, valor)

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
