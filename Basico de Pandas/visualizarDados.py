import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('./transferencias - 05_2023.csv')

# Remover a coluna "ANO / MÊS"
df = df.drop(columns=['ANO / MÊS'])

# Converter a coluna "VALOR TRANSFERIDO" para tipo numérico (float)
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)

# Agrupar por tipo de favorecido e somar os valores transferidos
grupo_favorecido = df.groupby('TIPO FAVORECIDO')['VALOR TRANSFERIDO'].sum()

# Criar o gráfico de barras
plt.bar(grupo_favorecido.index, grupo_favorecido.values)

# Rotular o eixo x com os nomes dos tipos de favorecido
plt.xlabel('Tipo de Favorecido')

# Rotular o eixo y com "Valor Transferido"
plt.ylabel('Valor Transferido')

# Dar um título ao gráfico
plt.title('Valores Transferidos por Tipo de Favorecido')

# Exibir o gráfico
plt.show()
