"""Documento sobre manipulação de documentos utilizando NumPy"""
import numpy as np

# Para ace3ssar e manipular os dados de um array utilizamos em grande parte indexadores
arr = np.array([1, 2, 3, 4, 5])
# Imprime o elemento presente na posição '2' do array, ou seja: 3
print(arr[2])

# Indexadores podem ser utilizados com índices negativos para percorrer a lista pelo final
# Imprime o último elemento do array
print(arr[-1])

# Os indexadores funcionam para arrays de n-dimensões
dim_dois = np.array([[1,2],[3,4]])
# Imprime  elemento presenta na posição '1' do segundo array, ou seja: 4
print(dim_dois[1,1])

# É possível repartir arrays da seguinte forma, [início, fim, intervalo]
inteiros = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Imprimindo somento os números pares do array
print(inteiros[0:10:2])

# Imprimindo somento os números impares do array
print(inteiros[1:10:2])

# Tipos de dados, em numpy temos um método que retorna o tipo de dado do array
# Os tipos de dados possíveis em um array do NumPy são:
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type

# Imprime o tipo de dado do array
print(arr.dtype)

# É possível criar um array com um tipo de dado pré definido
# No caso abaixo o NumPy já realiza a conversão de inteiro para string
arr = np.array([0, 1, 2], dtype='S')
print(arr.dtype)

# Obs: Caso não seja possível converter o dado o NumPy levanta um "ValueError"

# Para os tipos de dados: i, u, f, S e U é possível definir o tamanho que sera ocupado em bytes

# Criando um array de inteiros de 2 bytes
arr = np.array([0, 1, 2], dtype='i2')
print(arr.dtype)

# É possível converter o tipo de dado de um array após a sua criação

# Criando array de strings
arr = np.array([0, 1, 2], dtype='S')
print(arr.dtype)

# Repassando array como inteiros de 8 bytes
arr = arr.astype('i8')
print(arr.dtype)

# Método Copy, copia o array para uma nova variável
arr = np.array([0, 1, 2], dtype='S')
arr_copy = arr.copy()

print(f'{arr}' + " = " + f'{arr_copy}')

# Método View, copia o array para uma nova variável 
# porém quando um array é alterado o outro sofre a mesma alteração
arr = np.array([0, 1, 2], dtype='S')
arr_view = arr.view()
arr[0] = '2'

print(f'{arr}' + " = " + f'{arr_view}')
