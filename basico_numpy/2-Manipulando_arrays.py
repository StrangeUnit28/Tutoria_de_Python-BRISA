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
