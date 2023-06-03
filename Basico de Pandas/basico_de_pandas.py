import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('./transferencias - 05_2023.csv')

# Remover a coluna "ANO / MÊS"
df = df.drop(columns=['ANO / MÊS'])

# Converter a coluna "VALOR TRANSFERIDO" para tipo numérico (float)
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)

# Exibir o DataFrame resultante
print(df)
