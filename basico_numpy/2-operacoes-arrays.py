import numpy as np


# Operações aritméticas com arrays
print("\nOperações aritméticas:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Soma elemento por elemento
print(arr1 - arr2)  # Subtrai elemento por elemento
print(arr1 * arr2)  # Multiplica elemento por elemento
print(arr1 / arr2)  # Divide elemento por elemento

# Funções matemáticas com arrays
print("\nFunções matemáticas:")
print(np.sum(arr1))  # Soma todos os elementos do arr1
print(np.mean(arr1))  # Calcula a média dos elementos do arr1
print(np.max(arr1))  # Retorna o valor máximo do arr1
print(np.min(arr1))  # Retorna o valor mínimo do arr1

# Operações de reshaping
print("\nOperações de reshaping:")
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.reshape(3, 2))  # Redimensiona o arr3 para ter 3 linhas e 2 colunas
print(arr3.flatten())  # Retorna uma versão achatada do arr3
