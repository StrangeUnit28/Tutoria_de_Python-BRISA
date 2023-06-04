import pandas as pd

"""
    A biblioteca pandas é uma das principais bibliotecas do Python para manipulação 
    e análise de dados. Nesse arquivo veremos a criação de um Data Frame (df), ou seja, 
    uma matriz com linhas e colunas, a partir de diferentes tipos de arquivos 
"""

# Criando um Data Frame de um arquivo .csv
df = pd.read_csv('dados.csv')

# Criando um Data Frame de um arquivo .json
df = pd.read_json('dados.json')

# Criando um Data Frame de um arquivo .html
dfs = pd.read_html('https://www.example.com/tabela.html')

# Criando um Data Frame de um arquivo .xlsx
df = pd.read_excel('dados.xlsx')
