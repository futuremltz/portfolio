# IA e Dados — Portfólio

Projetos de análise de dados, machine learning, deep learning e IA generativa, do tratamento de dados reais até modelos colocados em uso por meio de APIs e aplicativos.

Cada projeto fica em sua própria pasta, com README próprio descrevendo os dados, a abordagem, os resultados e as limitações.

## Projetos

| # | Projeto | Área | Ferramentas | Nível | Status |
| --- | --- | --- | --- | --- | --- |
| 01 | [Análise de dados públicos](./01-analise-dados-publicos) | Análise de dados | Python, pandas, SQL | Iniciante | Planejado |
| 02 | [Dashboard interativo](./02-dashboard-interativo) | Visualização | Python, Streamlit | Iniciante | Planejado |
| 03 | [Previsor de preços](./03-previsor-de-precos) | ML clássico | scikit-learn | Iniciante/Intermediário | Planejado |
| 04 | [Classificador de sentimento PT-BR](./04-classificador-sentimento) | NLP | Hugging Face | Intermediário | Planejado |
| 05 | [Sistema de recomendação](./05-sistema-recomendacao) | ML | pandas, PyTorch | Intermediário | Planejado |
| 06 | [Detector de objetos](./06-detector-de-objetos) | Visão computacional | PyTorch, YOLO, OpenCV | Intermediário | Planejado |
| 07 | [Chatbot RAG sobre documentos](./07-chatbot-rag) | IA generativa | API de LLM, banco vetorial | Intermediário | Planejado |
| 08 | [Pipeline ETL automatizado](./08-pipeline-etl) | Engenharia de dados | Airflow/Prefect, SQL, Docker | Intermediário | Planejado |
| 09 | [Rede neural do zero](./09-rede-neural-do-zero) | Deep learning | NumPy, C++ | Intermediário/Avançado | Planejado |
| 10 | [Previsão de séries temporais](./10-series-temporais) | Séries temporais | statsmodels, PyTorch | Avançado | Planejado |
| 11 | [Agente de IA com ferramentas](./11-agente-ia) | IA generativa | Python, API de LLM | Avançado | Planejado |
| 12 | [Mini GPT do zero](./12-mini-gpt) | Deep learning | PyTorch | Avançado | Planejado |
| 13 | [Detecção de fraude](./13-deteccao-fraude) | ML clássico | scikit-learn, XGBoost | Intermediário | Planejado |
| 14 | [Transcrição e resumo de áudios](./14-transcricao-audio) | Áudio / IA generativa | Whisper, API de LLM | Intermediário | Planejado |
| 15 | [Modelo no celular ou Raspberry Pi](./15-modelo-na-borda) | IA na borda | ONNX, TFLite | Avançado | Planejado |
| 16 | [Ajuste fino de modelo de imagem](./16-lora-imagens) | IA generativa | diffusers | Avançado | Planejado |
| 17 | [MLOps com monitoramento e retreino](./17-mlops) | MLOps | MLflow, Evidently | Avançado | Planejado |

> Status: **Planejado** → **Em andamento** → **Concluído**. Atualize a tabela conforme avança.

## Tecnologias

- **Linguagens:** Python, SQL, C++
- **Dados:** pandas, NumPy, Polars
- **Modelagem:** scikit-learn, XGBoost, PyTorch, Hugging Face
- **Visualização:** Matplotlib, Plotly, Streamlit
- **Produção:** FastAPI, Docker, Airflow, MLflow

## Estrutura do repositório

```
ia-e-dados/
├── README.md                  ← este arquivo
├── 01-analise-dados-publicos/
│   ├── README.md
│   ├── data/                  ← dados brutos (ou script para baixá-los)
│   ├── notebooks/             ← exploração
│   ├── src/                   ← código reutilizável
│   └── requirements.txt
├── 02-dashboard-interativo/
└── ...
```

## Padrão de cada projeto

1. **Problema** — a pergunta que o projeto responde
2. **Dados** — fonte, tamanho, licença e como foram tratados
3. **Abordagem** — baseline simples primeiro, depois o modelo final
4. **Resultados** — métricas, gráficos e análise de erros
5. **Limitações** — onde o modelo falha e por quê
6. **Como reproduzir** — ambiente, comandos e seeds

> Arquivos de dados grandes e modelos treinados não vão para o Git: use scripts de download ou Git LFS.

## Contato

- LinkedIn: [seu-perfil](https://linkedin.com/in/seu-perfil)
- E-mail: seu-email@exemplo.com
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
