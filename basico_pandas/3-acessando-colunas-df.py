import pandas as pd

"""
    A biblioteca pandas é uma das principais bibliotecas do Python para manipulação 
    e análise de dados. Nesse arquivo veremos algumas operações sobre
    colunas de um Data Frame 
"""

# Cria um Data Frame 
df = pd.read_csv('../exercicios/transferencias - 05_2023.csv')

# Cria um Series a partir de uma coluna do Data Frame
series_uf = df['UF']
print("Tipo objeto series_uf: ", end="")
print(type(series_uf))

# Cria um Data Frame a partir de mais de uma coluna do Data Frame
df_uf_municipio_orgao = df[['UF', 'NOME MUNICÍPIO', 'NOME ÓRGÃO']]
print("Data Frame df_uf_municipio_orgao: ")
print(df_uf_municipio_orgao)

# Dados da linha de índice 0
print("Dados da linha de índice 0")
print(df.loc[0])

# Dados das linhas pares de 0 ao 10
print("Dados das linhas pares de 0 ao 10")
print(df.loc[0:10:2])

# Mostrando os valores únicos da coluna uf
print("Valores únicos da coluna UF")
print(df['UF'].unique())