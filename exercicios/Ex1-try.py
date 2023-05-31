import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("transferencias.csv")

# remove a coluna de ano e mes

data = data.drop(columns=['ANO / MÊS'], axis=1)

# converta a coluna "valor transferido" para float
data["VALOR TRANSFERIDO"] = (
    data["VALOR TRANSFERIDO"].str.replace(",", ".").astype(float)
)

# utilizando o numpy, calcule o valor maximo, minimo, media da coluna valor transferido
maximo = np.max(data["VALOR TRANSFERIDO"])
minimo = np.min(data["VALOR TRANSFERIDO"])
media = np.mean(data["VALOR TRANSFERIDO"])

print("Valor maximo: ", maximo)
print("Valor minimo: ", minimo)
print("Valor medio: ", media)
# crie um grafico do matplotlib com o valor transferido por mes
plt.plot(data["VALOR TRANSFERIDO"], data["TIPO FAVORECIDO"])

plt.title('Meu Gráfico')
plt.show()

plt.plot(data["VALOR TRANSFERIDO"], data["NOME FAVORECIDO"])

plt.title('Meu Gráfico2')
plt.show()

