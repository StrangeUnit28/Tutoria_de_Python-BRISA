nome = input('Digite seu nome: ')

# Aqui estamos concatenando strings
# Importante ressaltar que o sinal de '+' não da espaço entre as strings, caso queria ter espaço entre elas digite
print("Olá "+ nome + ", tudo bem ?")

peso = input('Qual seu peso em kg: ')
peso_kg = int(peso)
peso_libras = peso_kg * 2.2046
# A função str() transforma o valor passado como parametro em string
print("Seu peso em libras é: " + str(peso_libras))

