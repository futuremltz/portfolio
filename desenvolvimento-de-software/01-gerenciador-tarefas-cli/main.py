<<<<<<< HEAD

print("Gerenciador de tarefas v0.1")
=======
import sys

tarefas = [
  {"titulo":"Limpar", "feita": False, "prioridade": "alta"},
  {"titulo": "Arrumar casa", "feita": False, "prioridade": "alta"}
]

def criar_tarefa(titulo, prioridade="media"):
    return {"titulo":titulo,"feita": False, "prioridade": prioridade}

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
  if len(sys.argv) > 1:
    comando = sys.argv[1]
    if len(sys.argv > 3):
      if comando.lower() == "add":
          tarefas.append(criar_tarefa(sys.argv[2], sys.argv[3]))
          print(f"Tarefa adicionada {sys.argv[2]} com prioridade {sys.argv[3]}")
    elif comando.lower() == "add":
        tarefas.append(criar_tarefa(sys.argv[2]))
        print(f"Tarefa adicionada {sys.argv[2]}")
    elif comando.lower() == "list":
        listar_tarefas(tarefas)

    elif comando.lower() == "done":
        concluir_tarefa(sys.argv[2])
        listar_tarefas(tarefas)

    else:
        print(f"Comando desconhecido: {comando}")
  else:
      print("Uso: python3 argumentos.py <comando>")


if __name__ == "__main__":
  main()
>>>>>>> 6c3ed56 (Atualizando)
