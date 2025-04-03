import pandas as pd
import os

# Define o diretório raiz como a pasta onde o script está (guardiao-cooperativo)
raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho do CSV a partir da raiz
caminho_csv = os.path.join(raiz_projeto, "data", "PS_20174392719_1491204439457_log.csv")

# Lê o CSV
dados = pd.read_csv(caminho_csv)

# Pega as primeiras 1000 linhas
dados_reduzidos = dados.head(1000)

# Adiciona coluna mensagem_recebida
mensagens = ["Tudo ok", "Confirme sua senha", "Pague agora", "Transferência urgente"] * 250
dados_reduzidos["mensagem_recebida"] = mensagens

# Salva novo CSV na pasta data
caminho_novo_csv = os.path.join(raiz_projeto, "data", "transacoes_reduzidas.csv")
dados_reduzidos.to_csv(caminho_novo_csv, index=False)

# Mostra as primeiras 5 linhas
print("Primeiras 5 transações com mensagem:")
print(dados_reduzidos.head())