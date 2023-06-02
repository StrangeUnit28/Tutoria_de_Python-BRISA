# Tutorial Básico de Utilização da Biblioteca Pandas em Python

Segue aqui um tutorial básico de como utilizar a biblioteca Pandas.

## Passo 1: Instalação do Pandas

Antes de começar, certifique-se de ter o Pandas instalado em seu ambiente Python. Você pode instalá-lo usando o seguinte comando no terminal:

```
 pip install pandas 
 ```

## Passo 2: Importando o Pandas

Importe o Pandas no início do seu código Python usando o comando:

``` 
import pandas as pd 
```

## Passo 3: Carregando dados em um DataFrame

O Pandas oferece a estrutura de dados DataFrame, semelhante a uma tabela. Você pode carregar dados em um DataFrame de varias maneiras, como um arquivo CSV, uma planilha do Excel ou um banco de dados. Veja como carregar dados de um arquivo CSV.No codigo de exemplo utilizaremos um arquivo csv, o mesmo utilizado no exercicio 1.

``` 
df = pd.read_csv('dados.csv')
 ```

Este comando irá ler o arquivo 'transferencias - 05_2023.csv' e carregar os dados em um DataFrame com o nome 'df'.

## Passo 4: Explorando os dados

Apos termos carregado os dados no nosso DataFrame o Panas nos permite utilizar varias funções e atributos para a manipulação dos dados como :

- Visualizar as primeiras linhas do DataFrame:

``` 
df.head()
```

- Visualizar as últimas linhas do DataFrame:

```
df.tail()
```

- Visualizar um resumo estatístico dos dados:

``` 
df.describe()
```

- Acessar uma coluna específica do DataFrame:

``` 
df['nome_da_coluna']
```


- Filtrar linhas com base em uma condição:

``` 
df[df['coluna'] > valor]
```

## Passo 5: Manipulando os dados

Alem dos metodos e atributos acima o panas tambem fornece recursos para manipular e transformar os dados. Aqui estão algumas operações comuns como:

- Adicionar uma nova coluna ao DataFrame:

```
df['nova_coluna'] = valor
```

- Excluir uma coluna do DataFrame:

```
df.drop('nome_da_coluna', axis=1, inplace=True)
```

- Ordenar o DataFrame com base em uma coluna:

```
df.sort_values('nome_da_coluna', ascending=False, inplace=True)
```

- Agrupar e resumir os dados:

```
df.groupby('nome_da_coluna').mean()
```

### Obs: Os metodos possuem diversos atributos podendo ter mais funções ainda do que as vistas desse modo e recomendado consultar a documentação caso seja necessario aplicações expecificas.

## EXTRA : Salvando os dados

Depois de manipular e transformar os dados, você pode salvar o DataFrame em um arquivo usando o seguinte comando:

```
df.to_csv('novo_dados.csv', index=False)
```

Este comando irá salvar o DataFrame em um arquivo CSV chamado 'novo_dados.csv'.

