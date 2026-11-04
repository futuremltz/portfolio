# ✅ Gerenciador de Tarefas CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-yellow)

> 🚧 **Em andamento.** Quando estiver pronto, este projeto vai para um repositório próprio.

Gerenciador de tarefas de linha de comando em Python: adicionar, listar e concluir tarefas direto pelo terminal.

## 🚀 Como executar

```bash
python3 main.py add "Estudar C++" alta   # adiciona tarefa (prioridade opcional: baixa, media, alta)
python3 main.py list                     # lista as tarefas
python3 main.py done 1                   # marca a tarefa 1 como concluída
```

## ✔️ Já funciona

- [x] Comando `add <titulo> [prioridade]`
- [x] Comando `list`
- [x] Comando `done <numero>`
- [x] Mensagem de uso quando nenhum comando é passado

## 🔜 Próximos passos

- [ ] Salvar as tarefas em arquivo (JSON) para não perder ao fechar o programa
- [ ] Mostrar a prioridade na listagem e ordenar por ela
- [ ] Comando `remove <numero>`
- [ ] Tratar erros de entrada (número inválido, título faltando)
- [ ] Testes com `pytest`
- [ ] GIF de demonstração
