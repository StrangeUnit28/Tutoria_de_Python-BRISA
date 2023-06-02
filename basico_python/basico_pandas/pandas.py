import pandas as pd #importando a biblioteca

#PARA VISUALIZAR DETERMINADA AÇÃO NO TERMINAL BASTA DESCOMENTAR (retirar o '#')

df = pd.read_csv('exercicios\transferencias - 05_2023.csv') #le o csv transferencias - 05_2023 do exercicio 1

#print(df.head()) #Visualiza as primeiras linhas do DataFrame com os dados do csv

#print(df.tail())#Visualiza as ultimas linhas do DataFrame com os dados do csv

#print(df.describe()) # Apresenta um resumo dos dados do DataFrame

#print(df['ANO / MÊS']) #imprime a coluna ANO/MES do dataframe

#print(df[df['NOME UNIDADE GESTORA'] == 'MINISTERIO DO PLANEJAMENTO E ORCAMENTO - Unidades com vínculo direto']) #imprime somente as linhas que possuem como unidade gestora o MINISTERIO DO PLANEJAMENTO E ORCAMENTO - Unidades com vínculo direto

df['nova coluna']  = 1455
#print(df['nova coluna'])
 

df.drop('ANO / MÊS', axis=1, inplace=True) #exclui a coluna ANO/MES do DataFrame
#print(df)

# df.sort_values('nome_da_coluna', ascending=False, inplace=True) Ordena uma coluna especifica do dataframe o que nao e tao pertintente nesse caso
print(df.groupby('ANO / MÊS').mean()) #imprime o agrupamento e resumo de dados



