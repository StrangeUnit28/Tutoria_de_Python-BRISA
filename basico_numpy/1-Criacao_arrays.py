"""Documento sobre criação de arrays utilizando numpy"""
import numpy as np

# Após importar o módulo é possível criar arrays que sejam capazes de utilizar todos os métodos do módulo numpy

# Criando array de 1 a 5
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Obs: também é possível criar um array utilizando tuplas
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# Dimensões, numpy permite a criação de arrays com n-dimensões

# Criação de array com dimensão 0
dim_zero = np.array(0)

# Criação de array com dimensão 1 para representar listas e tensores
dim_um = np.array([0, 1])

# Criação de array com dimensão 2 para representar matrizes e tensores
dim_dois = np.array([[0,1],[0,1]])

# É possível com o numpy verificar o número de dimensões de um array a partir do método 'ndim'
print(np.ndim(dim_zero))
print(np.ndim(dim_um))
print(np.ndim(dim_dois))

# Para a criação de arrays com n dimensões é possível utilizar o método 'ndim' novamente
dim_seis = np.array([0, 1, 2, 3, 4, 5], ndmin=6)
print(dim_seis)
