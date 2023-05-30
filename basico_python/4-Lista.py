"""
Para escrever uma lista em python, basta criar uma variável e escolher os 
valores que quiser alocar nela posicionando eles entre '[ ]' e separados por vírgula
"""

num = 14.54
lista1 = [11.5," Church", num]
print(lista1)

# Existem também as listas dentro de listas 
lista2 = [
    ["valor", 250],
    ["valor2", 300]
]
# Para acessar uma lista interna, basta passar seu índice entre '[ ]'. Lembrando o índice começa em 0
print(lista2[1])

# As listas podem ter todos os tipos de dados dentro delas(string, inteiro, float, [...])
lista3 = ['lisa', 1.74, 'emma', 1.68, 'mom', 1.83]
# A função del(data), exclui da lista o termo que lhe foi passado como argumento
del(lista3[2])

# Concatenando duas listas e alocando em outra variável
lista4 = lista3 + ['dad', 3.5 ]
print(lista4)


x = [2, 3, 4, 5, 7]
# Alocou a lista de 'x' em 'y'
y = list(x)
# Deletando o terceiro termo da lista 'y'
del(y[2])
# Alterando o valor do quarto termo da lista 'y'
y[3]= "24"
print(y)