def menu(*funcoes):
    cabecalho("Lista de Tarefas Pesoais")
    for i, v in enumerate(funcoes):
        print(f"{i+1} - {v}")

    linha()
    while True:
        escolha = leia_int("Digite a opção desejada: ")
        if 1 <= escolha <= len(funcoes):
            return escolha
        else:
            print("Opção Inválida!")


def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print("Digite um número inteiro válido!")
            continue


def linha(argumento="-", tamanho=45):
    print(argumento * tamanho)


def cabecalho(texto):
    linha()
    print(texto.center(45))
    linha()


def verifica_banco(caminho):
    try:
        with open(caminho, "r"):
            # conteudo = banco.read
            print("Banco existe e foi aberto!")

    except FileNotFoundError:
        with open(caminho, "w"):
            # conteudo = banco.read
            print("Banco criado com sucesso!")


def carregar_tarefas(arq):
    try:
        with open(arq, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            lista = []

            for valor in linhas:
                descricao, status_temp = valor.strip().split(";")
                status = status_temp == "True"

                lista.append({"descricao": descricao, "concluida": status})

            return lista

    except FileNotFoundError:
        print(f"Arquivo {arq} não encontrado!")
        return []


def salvar_tarefas(arq, lista):
    try:
        with open(arq, "w", encoding="utf-8") as arquivo:
            for linha in lista:
                arquivo.write(f"{linha['descricao']};{linha['concluida']}\n")
    except Exception:
        print("Ocorreu um erro inesperado")


def adicionar_tarefas(arq, descricao):
    try:
        lista = carregar_tarefas(arq)
        lista.append({"descricao": descricao, "concluida": False})
        salvar_tarefas(arq, lista)
    except Exception:
        print("Ocorreu um erro ao adicionar a tarefa!")
    else:
        print("Tarefa adicionada com sucesso.")


def marcar_concluida(arq, index):
    try:
        lista = carregar_tarefas(arq)
        lista[index - 1]["concluida"] = True
        salvar_tarefas(arq, lista)
    except Exception:
        print("Ocorreu um erro ao marcar a tarefa!")
    else:
        print("Tarefa marcada como concluida.")


def remover_tarefas(arq, index):
    try:
        lista = carregar_tarefas(arq)
        lista.pop(index - 1)
        salvar_tarefas(arq, lista)
    except Exception:
        print("Ocorreu um erro ao remover a tarefa!")
    else:
        print("Tarefa removida como concluida.")
