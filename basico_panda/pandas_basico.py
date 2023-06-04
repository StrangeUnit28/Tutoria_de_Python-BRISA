# Obs.: Para rodar este arquivo, é necessário instalar o pandas e o openpyxl, para abrir os arquivos .xlsx.
# Obs.: Para ver como está a tabela a qualquer momento, basta utilizar o método print(nome_dataframe).
# Primeiro, deve-se importar o panda no arquivo. 
import pandas as pd
import os

# ----------------------------------------------------------------------------------
# Criando um dataframe, um dataframe é nada mais que uma tabela dentro do python.
# Existem 3 métodos.

# Primeiro - DateFrame vazio.
dateframe = pd.DataFrame()

# Segundo - A partir de um dicionário do python.
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
        }

vendas_df = pd.DataFrame(venda) 

# Terceiro - A partir de um arquivo de dados.
vendas_df = pd.read_excel(os.getcwd()+'/basico_panda/'+"Vendas.xlsx")

# ----------------------------------------------------------------------------------
# Resumos de Visualização de Dados simples e úteis.
# head - mostra as x primeiras linhas (5 por default).
# shape - mostra a qtd de linhas e colunas.
# describe - mostra diversas funções (mean, count, std, min, etc) aplicadas nas colunas númericas.

print(vendas_df.head(10))
print(vendas_df.shape)
print(vendas_df.describe())

# ----------------------------------------------------------------------------------
# Pegar colunas da tabela.
produtos = vendas_df['Produto']
produtosComLoja = vendas_df[['Produto', 'ID Loja']]

# ----------------------------------------------------------------------------------
# Pegar linhas, valores especificos ou buscas mais complexas - função loc.
# pegar uma linha.
print(vendas_df.loc[1])

# pegar linhas que correspondem a uma condição.
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']

# pegar várias linhas e colunas usando o loc.
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ["ID Loja", "Produto", "Quantidade"]]

# pegar 1 valor específico, exemplo, pegar o que está na linha 1, na coluna 'Produto'.
print(vendas_df.loc[1, 'Produto'])

# ----------------------------------------------------------------------------------
# Adicionando colunas.
# Ao adicionar uma coluna, se ela existir, o pandas irá substituir os valores, caso não exista, irá adicionar a nova coluna.
# a partir de uma coluna que existe, ou seja, os dados de comissão serão tragos da coluna 'Valor Final'.
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05

# criar uma coluna com valor padrão, sem ser proveninente de outra coluna.
# ':' significa todas linhas.
vendas_df.loc[:, "Imposto"] = 0

# ----------------------------------------------------------------------------------
# Adicionando linhas
# Vamos adicionar as vendas de dezembro, para isso, utilizamos o método concat.
vendas_dez_df = pd.read_excel(os.getcwd()+'/basico_panda/'+"Vendas - Dez.xlsx")
vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True)

# ----------------------------------------------------------------------------------
# Excluindo linhas e colunas axis pode ser 0 e 1, use 1 para colunas e 0 para linhas, o default é 0.
# Coluna
vendas_df = vendas_df.drop('Imposto', axis=1)
# Linhas
vendas_df = vendas_df.drop(0, axis=0)

# ----------------------------------------------------------------------------------
# Tratar valores vázios. 

# Deletar linhas/colunas vazias.
# Deletar linhas que possuem valores vazios. 
# Preencher valores vazios (média e último valor).

# deletar linhas e colunas completamente vazias.
vendas_df = vendas_df.dropna(how='all', axis=1)

# deletar linhas que possuem pelo menos 1 valor vazio.
vendas_df = vendas_df.dropna()

# preencher com a média da coluna.
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())

# preencher com o último valor acima dele, exemplo:
# Produto 1
# X
# Produto 2
# Y
# X será preenchido com Produto 1 e Y por produto 2.
vendas_df = vendas_df.ffill()

# ----------------------------------------------------------------------------------
# Calculando indicadores
# Value counts - Fazer alguma contagem, no nosso exemplo, podemos calcular quantas vezes x loja apareceu
transacoes_loja = vendas_df['ID Loja'].value_counts()
# Group by - Agrupar as informações, no nosso exemplo, o faturamento dos produtos, fazendo a soma dos valores finais de todos produtos
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()

# ----------------------------------------------------------------------------------
# Mesclar dataframes
# Podemos mesclar dataframes, no nosso exemplo, queremos mesclar os gerentes das lojas com os dados da venda.
# Como o arquivo 'Gerentes.xlsx' possui uma coluna igual ao que temos na 'Vendas.xlsx', o pandas consegue fazer o merge automaticamente.
gerentes_df = pd.read_excel(os.getcwd()+'/basico_panda/'+"Gerentes.xlsx")
vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)