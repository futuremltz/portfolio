titulo = "=== Gerenciador de Tarefas ==="
mensagem = "Boas-vindas"

print(titulo)
print(mensagem)

nome = input("Qual o seu nome? ")
print(f"Prazer, {nome}")

tarefa = input("Qual tarefa deseja adicionar? ")
prioridade = int(input("Prioridade (1 a 3): "))
minutos_estimados = int(input("Tempo estimado (em minutos): "))

horas_estimadas = round(minutos_estimados / 60, 2)

print()
print(f"Tarefa adicionada: {tarefa}")
print(f"Prioridade: {prioridade}")
print(f"Tempo estimado: {minutos_estimados} min ({horas_estimadas} h)")
