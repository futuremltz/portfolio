import sys
import json
import os

dados_arquivos = "tarefas.json"


def criar_tarefa(titulo, prioridade="media"):
    return {"titulo": titulo, "feita": False, "prioridade": prioridade}


def formatar_tarefa(numero, tarefa):
    status = "x" if tarefa["feita"] else " "
    return f"{numero}. [{status}] {tarefa['titulo']}"


def listar_tarefas(tarefas):
    for numero, tarefa in enumerate(tarefas, start=1):
        texto = formatar_tarefa(numero, tarefa)
        print(texto)


def concluir_tarefa(tarefas, numero):
    try:
        tarefas[numero - 1]["feita"] = True
        return True
    except IndexError:
        print("Erro: Número de tarefa inválido.")
        return False


def carregar_tarefas():
    if not os.path.exists(dados_arquivos):
        return []

    try:
        with open(dados_arquivos, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_tarefas(tarefas):
    with open(dados_arquivos, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)


def main():
    tarefas = carregar_tarefas()

    print("Gerenciador de tarefas v0.2")

    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        if comando == "add":
            titulo = sys.argv[2]
            if len(sys.argv) > 3:
                tarefa = criar_tarefa(titulo, sys.argv[3])
            else:
                tarefa = criar_tarefa(titulo)
            tarefas.append(tarefa)

            salvar_tarefas(tarefas)

            print(f"Tarefa adicionada: {titulo}")

        elif comando == "list":
            listar_tarefas(tarefas)

        elif comando == "done":
            if len(sys.argv) < 3:
                print("Erro: Informe o número da tarefa.")
                return

            numero_tarefa = int(sys.argv[2])

            if concluir_tarefa(tarefas, numero_tarefa):
                salvar_tarefas(tarefas)
                print(f"Tarefa {numero_tarefa} marcada como concluída!")
                listar_tarefas(tarefas)

        else:
            print(f"Comando desconhecido: {comando}")
    else:
        print("Uso: python3 main.py <comando>\n")
        print(
            "Comandos disponíveis:\n add <titulo> [prioridade] \n list \n done <numero>"
        )


if __name__ == "__main__":
    main()
