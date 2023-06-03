import pandas as pd
import numpy as np

# Carregar o arquivo CSV
df = pd.read_csv('./transferencias - 05_2023.csv')

# Remover a coluna "ANO / MÊS"
df = df.drop(columns=['ANO / MÊS'])

# Converter a coluna "VALOR TRANSFERIDO" para tipo numérico (float)
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)

# Calcular o valor máximo da coluna "VALOR TRANSFERIDO"
valor_maximo = np.max(df['VALOR TRANSFERIDO'])

# Calcular o valor mínimo da coluna "VALOR TRANSFERIDO"
valor_minimo = np.min(df['VALOR TRANSFERIDO'])

# Calcular o valor médio da coluna "VALOR TRANSFERIDO"
valor_medio = np.mean(df['VALOR TRANSFERIDO'])

# Exibir os resultados
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Valor médio:", valor_medio)
