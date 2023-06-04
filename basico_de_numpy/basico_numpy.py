# Nesta linha, o módulo NumPy é importado com o alias 'np'. NumPy é uma biblioteca em 
# python utilizada para realizar operações numéricas eficientes em arrays multidimensionais.
import numpy as np

# Preencher arrays com valores especificos
pares = np.array([n for n in range(0, 101, 2)])  # Cria um array com números pares de 0 a 100
print(pares)

print(np.zeros(10))  # Cria um array de zeros com 10 elementos

print(np.ones(10))  # Cria um array de uns com 10 elementos

print(np.full(8, 12))  # Cria um array com 8 elementos, todos iguais a 12

print(np.zeros(10, dtype=int))  # Cria um array de zeros com 10 elementos, do tipo inteiro

print(np.ones(15, dtype=int))  # Cria um array de uns com 15 elementos, do tipo inteiro

print(np.full(8, 12, dtype=float))  # Cria um array com 8 elementos, todos iguais a 12, do tipo float

print(np.zeros((2,5), dtype=int))  # Cria uma matriz de zeros com 2 linhas e 5 colunas, do tipo inteiro

# Criar arrays a partir de faixas de valores: métodos arange e linspace

print(np.arange(10))  # Cria um array que vai de 0 a 9 (10 elementos no total)

print(np.arange(10.))  # Cria um array que vai de 0.0 a 9.0 (10 elementos no total), do tipo float

print(np.arange(5, 16))  # Cria um array que vai de 5 a 15 (11 elementos no total)

print(np.linspace(0.0, 2.0, num=5))  # Cria um array com 5 elementos espaçados uniformemente entre 0.0 e 2.0

# Arrays com valores aleatorios - Métodos rand e radint

a = np.random.rand(10)  # Cria um array com 10 números aleatórios entre 0 e 1
print(a)

c = np.random.rand(3,3)  # Cria uma matriz 3x3 com números aleatórios entre 0 e 1
print(c)

print('Números aleatórios', np.random.randint(9))  # Gera um número aleatório inteiro entre 0 e 8

b = np.random.randint(10, 21, size=10)  # Cria um array com 10 números aleatórios entre 10 e 20
print(b)

d = np.random.randint(1, 31, size=(4,5))  # Cria uma matriz 4x5 com números aleatórios entre 1 e 30
print(d)