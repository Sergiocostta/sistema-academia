import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dados do usuário
usuario = {
    "usuario": "joao",
    "senha": "abcd",
    "tipo": "aluno"
}

# Treinos prontos segundo o treino predefinido
treinos_prontos = {
    "2023-01-01": {
        "titulo": "Treino de Peito, Tríceps e Ombros",
        "descricao": "Treinamento completo focado nas porções do peitoral, tríceps e todas as porções dos ombros.",
        "series": 4,
        "exercicios": ["Supino reto com barra", "Supino inclinado com halteres", "Crucifixo reto com halteres", "Flexões de braço", "Triceps Pushdown com Corda", "Overhead Tricep Extension com Halteres", "Triceps Kickback com Halteres", "Diamond Push-Up", "Desenvolvimento com halteres", "Elevação lateral com halteres", "Elevação frontal com halteres", "Elevação posterior no banco inclinado"]
    },
    "2023-01-02": {
        "titulo": "Treino de Costas, Bíceps e Abdômen",
        "descricao": "Foco em largura e densidade das costas, força dos bíceps e estabilidade do core com exercícios para o abdômen.",
        "series": 4,
        "exercicios": ["Puxada frontal na polia alta", "Remada curvada com barra", "Remada unilateral com halteres", "Barra fixa (pegada pronada)", "Rosca direta com barra", "Rosca alternada com halteres", "Rosca concentrada", "Rosca martelo", "Prancha abdominal", "Abdominal infra com elevação de pernas", "Abdominal supra no solo", "Elevação de pernas na barra"]
    },
    "2023-01-03": {
        "titulo": "Treino de Pernas",
        "descricao": "Fortalecimento completo de membros inferiores com foco em quadríceps, posteriores, glúteos e panturrilhas.",
        "series": 4,
        "exercicios": ["Agachamento livre com barra", "Leg Press 45°", "Cadeira extensora"]
    },
}

# Simulando dados de treino com base nos treinos prontos
dados_treino = {
    "data": [],
    "exercicios_realizados": [],
    "series_realizadas": []
}

for data, treino in treinos_prontos.items():
    dados_treino["data"].append(pd.to_datetime(data))
    dados_treino["exercicios_realizados"].append(len(treino["exercicios"]))  # Contagem dos exercícios realizados
    dados_treino["series_realizadas"].append(treino["series"])  # Número de séries

# Criando um DataFrame
df = pd.DataFrame(dados_treino)

# Gerando gráficos
plt.figure(figsize=(10, 5))
plt.plot(df['data'], df['exercicios_realizados'], marker='o', label='Exercícios Realizados')
plt.plot(df['data'], df['series_realizadas'], marker='s', label='Séries Realizadas')
plt.title('Progressão dos Treinos - Usuário: {}'.format(usuario['usuario']))
plt.xlabel('Data')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('grafico_progressao.png')  # Salva o gráfico como imagem
plt.show()

# Gerando relatório semanal/mensal
relatorio_semanal = df.resample('W', on='data').sum()
relatorio_mensal = df.resample('M', on='data').sum()

print("Relatório Semanal:")
print(relatorio_semanal)

print("\nRelatório Mensal:")
print(relatorio_mensal)