import pandas as pd
import os
from tabulate import tabulate
from sklearn.ensemble import IsolationForest

# Define o diretório raiz
raiz_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_csv = os.path.join(raiz_projeto, "data", "transacoes_reduzidas.csv")

# Lê o CSV
dados = pd.read_csv(caminho_csv)

# Prepara os dados pro modelo
dados["mensagem_suspeita"] = dados["mensagem_recebida"].apply(
    lambda x: 1 if "senha" in x.lower() or "urgente" in x.lower() else 0
)
features = dados[["amount", "mensagem_suspeita"]]

# Cria e treina o modelo
modelo = IsolationForest(contamination=0.05, random_state=42)
modelo.fit(features)

# Prediz anomalias
dados["suspeita_ia"] = modelo.predict(features)
suspeitas = dados[dados["suspeita_ia"] == -1]

# Formata valores como monetário (R$)
suspeitas["amount"] = suspeitas["amount"].apply(lambda x: f"R$ {x:,.2f}")

# Mostra resultados
print("Transações suspeitas (IA):")
print(tabulate(suspeitas[["amount", "mensagem_recebida", "isFraud"]], 
               headers=["Valor", "Mensagem", "Fraude"], 
               tablefmt="grid", 
               showindex=False))

# Total de suspeitas
print(f"\nTotal de transações suspeitas: {len(suspeitas)}")

# Salva suspeitas
caminho_suspeitas = os.path.join(raiz_projeto, "data", "suspeitas_ia.csv")
suspeitas.to_csv(caminho_suspeitas, index=False)