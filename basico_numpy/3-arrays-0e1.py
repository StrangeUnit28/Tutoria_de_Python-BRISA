import numpy as np

"""O numpy também possui funções para criar arrays preenchidos com zeros e uns
semelhante ao calloc da linguagem C. Isso é útil para inicializar arrays que 
serão preenchidos posteriormente.
    """

# Criando arrays preenchidos com zeros e uns
print("\nArrays preenchidos com zeros e uns:")
arr_zeros = np.zeros((2, 3))  # Cria um array de zeros com 2 linhas e 3 colunas
print(arr_zeros)

arr_ones = np.ones((3, 2))  # Cria um array de uns com 3 linhas e 2 colunas
print(arr_ones)




