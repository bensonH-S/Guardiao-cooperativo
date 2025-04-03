import os

# Define a estrutura de pastas
estrutura = {
    "guardiao-cooperativoss": [
        "data",           # Para armazenar o CSV e outros dados
        "src",            # Código fonte (scripts Python)
        "models",         # Modelos de IA treinados
        "docs",           # Documentação e README
        "tests"           # Testes (opcional, pra futuro)
    ]
}

# Função para criar pastas
def criar_estrutura(base_path, estrutura):
    for pasta, subpastas in estrutura.items():
        # Cria a pasta principal
        caminho_pasta = os.path.join(base_path, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
            print(f"Criada pasta: {caminho_pasta}")
        
        # Cria as subpastas
        if isinstance(subpastas, list):
            for subpasta in subpastas:
                caminho_subpasta = os.path.join(caminho_pasta, subpasta)
                if not os.path.exists(caminho_subpasta):
                    os.makedirs(caminho_subpasta)
                    print(f"Criada subpasta: {caminho_subpasta}")

# Executa o script na pasta atual
base_path = os.getcwd()  # Pega o diretório atual
criar_estrutura(base_path, estrutura)

print("Estrutura de pastas criada com sucesso!")