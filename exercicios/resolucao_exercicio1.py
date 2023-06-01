import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataframe = pd.read_csv('transferencias.csv')

# Recebe moda de UF e substitui nas linhas que possuem valor nulo
uf_moda = dataframe['UF'].mode()[0]
dataframe.dropna(axis=1, inplace=True)

print(dataframe.head(2))

# Remova a coluna "ANO / MÊS".
dataframe.drop(columns=['ANO / MÊS'], inplace=True)

if 'ANO / MÊS' not in dataframe.columns:
    print(dataframe.columns, '\n')

# Substitua as vírgulas (",") por pontos (".") na coluna "VALOR TRANSFERIDO".
# Converta a coluna "VALOR TRANSFERIDO" para o tipo numérico (float).
print(type(dataframe['VALOR TRANSFERIDO'].values[0]))
dataframe['VALOR TRANSFERIDO'] = dataframe['VALOR TRANSFERIDO'].str.replace(
    ',', '.').astype(float)
print(type(dataframe['VALOR TRANSFERIDO'].values[0]),
      '\n', dataframe['VALOR TRANSFERIDO'])

valor_maximo = np.max(dataframe['VALOR TRANSFERIDO'])
valor_minimo = np.min(dataframe['VALOR TRANSFERIDO'])
valor_medio = np.mean(dataframe['VALOR TRANSFERIDO'])

print(f'Valor Máximo: {valor_maximo}')
print(f'Valor Mínimo: {valor_minimo}')
print(f'Valor Médio: {valor_medio}')

## Visualizar dados
# Filtrar colunas relevantes
dados_filtrados = dataframe[['TIPO FAVORECIDO', 'VALOR TRANSFERIDO']]

# Agrupar por tipo favorecido e calcular a soma dos valores transferidos
agrupado = dados_filtrados.groupby('TIPO FAVORECIDO')['VALOR TRANSFERIDO'].sum()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))  # Definir tamanho da figura
plt.bar(agrupado.index, agrupado.values)

# Personalizar o gráfico
plt.xlabel('Tipo Favorecido')
plt.ylabel('Valores Transferidos')
plt.title('Valores Transferidos por Tipo Favorecido')
plt.xticks(rotation=90)

# Melhorar a disposição dos elementos no gráfico
plt.tight_layout()

# Exibir o gráfico
plt.show()
