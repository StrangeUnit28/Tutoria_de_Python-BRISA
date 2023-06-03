#para verificar cada comando basta retirar o comentario antes dele (retirar o #)

import pandas as pd

#importa o arquivo csv e o transforma em um DataFrame
df = pd.read_csv('exercicios/transferencias - 05_2023.csv') 

#Visualiza as primeiras linhas do DataFrame com os dados do csv
#print(df.head()) 

#Visualiza as ultimas linhas do DataFrame com os dados do csv
#print(df.tail())

# Apresenta um resumo dos dados da coluna ANO/MES do DataFrame
#print(df.describe())

#imprime a coluna ANO/MES do dataframe
#print(df['ANO / MÊS']) 

#imprime somente as linhas que possuem como ValorTransferido 583145,98
#print(df[df['VALOR TRANSFERIDO'] == '583145,98']) 

#Cria uma nova coluna e atribui o valor 1455 a todas as linhas
df['nova coluna']  = 1455
#print(df['nova coluna'])

#Retira a coluna correspondente ao ano e mes do dataframe
df.drop('ANO / MÊS', axis=1, inplace=True) 
#print(df.columns)

#Ordena uma coluna especifica do dataframe o que nao e tao pertintente nesse caso
#df.sort_values('VALOR TRANSFERIDO', ascending=False, inplace=True) 
#print(df['VALOR TRANSFERIDO'])
