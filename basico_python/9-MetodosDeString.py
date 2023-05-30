string = 'Introdução ao python'

# A função len() retorna um inteiro que informa o tamanho da variável passada como parâmetro
print(len(string))

"""
As funções upper() e lower() retornam, respectivamente, a string passada 
como parâmetro escrita em letra maiúscula e escrita em letra minúscula
"""
print(string.upper())
print(string.lower())

# A função find() encontra o char passado como parâmetro e retorna seu índice 
print(string.find('p'))
print(string.find('python'))

# A função replace() substitui uma sequência de caracteres por outra, ambas passadas como parâmetro
print(string.replace('Introdução', 'Tutoria'))
