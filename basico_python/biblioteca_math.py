# A biblioteca math possui diversas funções que podem auxiliar nos cálculos
# para importar a biblioteca
import math

# Algumas dessas funções são:
# A função min() mostra o menor e a função max() o maior valor 

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y) 

# A função pow(x, y) retorna o valor de x elevado à potência de y (x^y)

x = 4
y = 3
a = pow(x, y)

print(a)

# A função abs() retorna o módulo de um número

c = abs(-7.25)

print(c)

#O Python também possui um módulo embutido chamado math, que estende a lista de funções matemáticas.
#Para usá-lo, você deve importar o módulo math:

#import math

#Depois de importar o módulo math, você pode começar a usar métodos e constantes do módulo.
# Depois de importar o módulo math, você pode começar a usar métodos e constantes do módulo.

# O método math.sqrt() por exemplo, retorna a raiz quadrada de um número:

b = math.sqrt(64)

print(b)

# O math.ceil arredonda um número para cima, enquanto math.floor arredonda um número para baixo

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1 
