# Um loop é uma estrutura de repetição, que é um conceito fundamental 
# em programação, o qual nos permite executar um bloco de código várias vezes

# 'for'
# O 'for' é usado para percorrer uma sequência. 
# Exemplo de algo que podemos percorrer seria uma lista, uma string ou um vetor
# Em resumo qualquer objeto que possamos repetir sequencialmente.

# Exemplo: Lista
jogos = ['cs', 'valorant', 'subway_surf']

for jogo in jogos:
    print(jogo)

# Saída:
# cs
# valorant
# subway_surf

# Exemplo: String
fruta = "Abacate"

for letra in fruta:
    print(letra)

# Saída:
# A 
# b 
# a 
# c 
# a 
# t 
# e

# 'while'
# O 'while' é usado para repetir um bloco de código 
# até que uma condição nao seja mais verdadeira.

contador = 0

while contador < 3:
    print("Contador = ", contador)
    contador += 1

# Saída:
# Contagem: 0
# Contagem: 1
# Contagem: 2

# Usando 'break' para sair do loop

contador = 0

while True:
    print("Contador = ", contador)
    contador += 1
    if contador == 3:
        break

# Saída:
# Contagem: 0
# Contagem: 1
# Contagem: 2

# Usando 'continue' para pular iterações

contador = 0

while contador < 5:
    contador += 1
    if contador == 2:
        continue
    print("Contador = ", contador)

# Saída:
# Contagem: 1
# Contagem: 3
# Contagem: 4
# Contagem: 5
