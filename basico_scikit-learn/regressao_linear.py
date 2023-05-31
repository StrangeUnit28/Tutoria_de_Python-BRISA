# Regressão linear é um dos modelos preditivos mais simples. O objetivo é predizer um determinado valor Y baseado em um valor X.

# Permite traçar uma linha que represente a relação linear entre a variável X (entrada) e a variável Y (Saída)

import pandas as pd
from matplotlib import pyplot as pit
from sklearn.datasets import make_regression # Cria dataset Random
from sklearn.linear model import LinearRegression # Pacote que realiza a regressão linear

# Gerando amostra random
x, y = make_regression (n_samples=200, n_ features=1,
noise=30)

# n_samples = Número de amostras
# n_features = Número de categorias
# noise = ruído

plt.scatter (x, y)

# Cria o modelo de regressão linear com base nos dados acima
modelo = LinearRegression()
modelo.fit (x, y)

# y = a + b*x
# y = l_coeff + a_coeff * x

# Coeficiente angular
a_coeff = modelo.coef
l_coeff = modelo.intercept_
# coeficiente linear
print ('Coeficiente Angular: (0) InCoeficiente Linear (1) '.format (a_coeff, 1 _coeff)) 


# Gráfico com os valores random
pit.scatter (x, y) 

# Plot da reta com os valores
plt.plot (x, l_coeff + a coeff*x, color=' red') 
plt.show () # Mostra a reta gerada da regressão linear
