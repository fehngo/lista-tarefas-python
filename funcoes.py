def verifica_banco(caminho):
    try:
        with open(caminho, "r"):
            # conteudo = banco.read
            print("Banco existe e foi aberto!")

    except FileNotFoundError:
        with open(caminho, "w"):
            # conteudo = banco.read
            print("Banco criado com sucesso!")


def adicionar_tarefas(caminho, tarefa):
    try:
        with open(caminho, "a+", encoding="utf-8") as banco:
            banco.write(f"{tarefa};{False}\n")
    except Exception:
        print("Tarefa não adicionada!")
    else:
        print("Tarefa adicionada com sucesso!")


def marcar(caminho, tarefa):
    try:
        with open(caminho, "a+", encoding="utf-8") as banco:
            banco.write(f"{tarefa}\n")
    except Exception:
        print("Tarefa não adicionada!")


def zerar_lista(caminho):
    try:
        with open(caminho, "w", encoding="utf-8"):
            pass
    except Exception:
        print("Houve um erro ao zerar a lista")


def ler_arquivo(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as banco:
            leitura = banco.readlines()
            return leitura
    except Exception:
        print("Ocorreu um erro ao ler o arquivo!")


def ler_linhas(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as banco:
            leitura = banco.readlines()
            return leitura
    except Exception:
        print("Ocorreu um erro ao ler o arquivo!")


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
