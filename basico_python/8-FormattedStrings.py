primeiro_nome = 'Douglas'
ultimo_nome = 'Dionísio'
msg1 = primeiro_nome + ' ' + ultimo_nome + ' é desenvolvedor' #string concatination
# Uma outra forma de colocar o valor de variáveis em outra ou mesmo no print é utilizando a formatted string
# A formatted string começa com um f e aloca o valor das variáveis entre '{ }'
msg2 = f'{primeiro_nome} {ultimo_nome} é desenvolvedor'
print(msg1)
print(msg2)