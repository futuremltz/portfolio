import sys


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
    tarefas[numero - 1]["feita"] = True


def main():
    tarefas = [
        criar_tarefa("Limpar", "alta"),
        criar_tarefa("Arrumar casa", "alta"),
    ]
    print("Gerenciador de tarefas v0.1")

    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()
        if comando == "add":
            titulo = sys.argv[2]
            if len(sys.argv) > 3:
                tarefa = criar_tarefa(titulo, sys.argv[3])
            else:
                tarefa = criar_tarefa(titulo)
            tarefas.append(tarefa)
            print(f"Tarefa adicionada: {titulo}")

        elif comando == "list":
            listar_tarefas(tarefas)

        elif comando == "done":
            concluir_tarefa(tarefas, int(sys.argv[2]))
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
