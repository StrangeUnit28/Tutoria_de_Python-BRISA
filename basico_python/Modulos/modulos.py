import matemagica

# Em python além de instalar módulos podemos cria-los
# O arquivo matemagica.py possui diversas funções matemáticas básicas
# O mesmo após ser criado pode ser importado e instânciando
# Desta forma é possível utilizar todas as funções nele contidas

# Instanciando o modulo
calculadora = matemagica

# Ira realizar a soma x + y
print(calculadora.soma(5, 5))

# Ira realizar a subtração de x - y
print(calculadora.sub(5, 5))

# Ira realizar a divisão de x / y
print(calculadora.div(5, 5))

# Ira realizar a multiplicação de x * y
print(calculadora.mul(5, 5))

# Obs: os módulos podem possuir qualquer tipo de função e não se limitam a apenas matemática