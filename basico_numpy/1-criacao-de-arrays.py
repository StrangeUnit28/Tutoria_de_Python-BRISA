# NUMPY

# Numpy é uma biblioteca em Python destinada a realizar operações em arrays multidimensionais.
# Por exemplo, não é possível declarar dois arrays e fazer a multiplicação ou a soma deles, porém, 
# na Numpy, temos métodos que nos permitem realizar estas e outras operações.

# Para utilizar a biblioteca, primeiro devemos importá-la
import numpy as np 

# Para começar a trabalhar com a biblioteca, vamos definir um array. 

# Podemos fazer dessa forma:
lista1 = [1, 2, 3, 4, 5]
primeiro_array = np.array(lista1)

# Ou dessa:
segundo_array = np.array([6, 7, 8, 9, 10])

# Para ver o array, podemos usar a função print
print(primeiro_array)
print(segundo_array)

# Para verificar o tamanho do array, podemos usar a função shape, que retorna uma tupla com a dimensão do array
print(primeiro_array.shape)
print(segundo_array.shape)

# Também podemos criar arrays bidimensionais e usar a função shape para ver sua quantidade de linhas e colunas
array_bidimensional = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(array_bidimensional.shape)

# A Numpy também possui uma variedade de funções para criar arrays, como por exemplo:

# Array de zeros
array_de_zeros = np.zeros((3, 4), dtype=int)
print(array_de_zeros)

# Array de 1s
array_de_1s = np.ones(5)
print(array_de_1s)

# Array de valores aleatórios
numeros_aleatorios = np.random.random((5)) 
print(numeros_aleatorios)
