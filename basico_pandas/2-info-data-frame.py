import pandas as pd

"""
    A biblioteca pandas é uma das principais bibliotecas do Python para manipulação 
    e análise de dados. Nesse arquivo veremos as informações de um Data Frame criado
"""

# Verifica o tipo de objeto criado
df = pd.read_csv('../exercicios/transferencias - 05_2023.csv')
print("Tipo objeto df")
print(type(df))

# Identifica quantas linhas e colunas do Data Frame
print("Linhas e Colunas Data Frame")
print(df.shape)

# Verifica as formato se encontram os dados em cada coluna, 
# além da quantidade de memória para ler esse conjunto de dados do Data Frame
print("Informações sobre Data Frame")
print(df.info())

# Visualiza a estatística dos dados do Data Frame
print(df.describe())

# Visualiza as colunas do Data Frame
print(df.columns)

# Visualiza as primeiras n linhas do Data Frame
print("As primeiras n linhas do Data Frame")
print(df.head(n=6))

# Visualiza as últimas n linhas do Data Frame
print("As últimas n linhas do Data Frame")
print(df.tail(n=6))
