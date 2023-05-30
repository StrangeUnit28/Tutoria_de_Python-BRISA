# A função input() permite que o usuário interaja com a aplicação por meio do terminal
# Ao mesmo tempo o dado passado ao input será alocado na variável 'senha'
# Input sempre retorna uma string
senha = input("Defina uma senha: ")
print("Senha registrada com sucesso!")

chances = 1

# While é uma estrutura de repetição que continua rodando até que a condição passada seja descumprida
while chances <= 3:
    senha_tentada = input("type pass: ")
    # If é uma estrutura condicional, onde a condição é passada entre parenteses
    # Dentro dos parenteses esta ocorrendo uma comparação de strings
    if (senha_tentada == senha):
        print("Acesso permitido")
        # Break nesse caso tira o processo da repetição do while, mesmo se a condição não tenha sido atingida
        break
    else:
        print("Senha incorreta")
    # Incrementando a variável utilizada como condição
    # Mesma coisa que -> chances += 1    
    chances = chances + 1