"""Documento sobre operadores em python"""

# Em python utilizamos operadores para realizar operações entre valores e variaveis

# Exemplo operador '+' realiza a soma entre 10 e 5 e o operador '=' armazena o valor da soma na variavel 'x'
x = 10 + 5

# Em python temos diversos tipos de operadores:

# Operadores aritméticos, são utilizados em contas matemáticas

# '+' = soma, '-' = subtração, '*' = multiplicação, '/' = divisão, '%' = módulo, '**' = exponenciação '//' = divisão interia

# Usos:

# Os 4 primeiros são bem conhecidos pois se assememlham ao que utilizamos na matemática
print("Soma (10 + 5) = " + f'{10 + 5}')
print("Subtração (10 - 5) = " + f'{10 - 5}')
print("Divisão (10 / 5) = " + f'{10/5}')
print("Multiplicação (10 * 5) = " + f'{10*5}')

# O operador '%' retorna o resto da divisão entre dois números
print("Módulo (10 % 5) = " + f'{10%5}')

# O operador '**' realiza a potenciação de um número x elevado a y
print("Exponenciação (10 ** 5) = " + f'{10 ** 5}')

# O operador '//' retorna somente a parte inteira da divisão entre dois números
print("Floor (11 // 5) = " + f'{11 // 5}')

# Operadores de atribuição, são utilizados para atribuir valores a variáveis
# O operador universal de atribuição é o '='

# Usos:

x = 10

# O operador de '=' pode ser combinado com operadores aritméticos e lógicos, assim reduzindo linhas de código
# Ao invés de escrever x = x + 10 podemos realizar podemos optar por:
x += 10
x -= 10 # x = x - 10
x *= 10 # x = x * 10
x /= 10 # x = x / 10

# Operadores de comparação, comparam 2 valores e retornam verdadeiro o falso
# '==' Igual, '!=' diferente, '>' maior, '<' menor, '>=' maior ou igual, '<=' menor ou igual

#Usos

# O principal uso é na tomada de decisões do código, por exemplo:
hora = 8
if hora == 8:
    print("Fim do expediente")

# Operadores lógicos, utilizados para combinar condicionais
# 'and' = e lógico, 'or' = ou lógico, 'not' negação

# and: retorna true se as condicionais são verdadeiras
if hora == 8 and x > 0:
    print("Já são 8 horas e x > 0")

# or: retorna true se qualquer condicional for veradeira
if hora == 5 or x > 0:
    print("Não são 5 horas mas x > 0")

# not: inverte o valor
if not(hora == 5 or x > 0):
    print("Print não ocorre pois a comparação de valor true foi negada")

