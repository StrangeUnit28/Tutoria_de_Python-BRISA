import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('transferencias - 05_2023.csv')

df = df.drop(columns=["ANO / MÊS"])
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.')
df["VALOR TRANSFERIDO"]= df["VALOR TRANSFERIDO"].astype('float')
valor_min = np.min(df['VALOR TRANSFERIDO'])
valor_max = np.max(df['VALOR TRANSFERIDO'])
media = np.mean(df['VALOR TRANSFERIDO'])
print(df)
print(
    "Valor minímo: " + f'{valor_min}' +
    "\nValor máximo: " + f'{valor_max}' +
    "\nMédia: " + f'{media}')

valores = df['VALOR TRANSFERIDO']
favorecidos = df['TIPO FAVORECIDO']
fig = plt.figure(figsize = (30, 15))

plt.bar(favorecidos, valores, color ='blue', width = 0.4)
plt.xlabel("Tipos Favorecidos")
plt.ylabel("Valor Transferido")
plt.title("Valores transferidos para cada tipo")
plt.show()
