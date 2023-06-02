import pandas as pd

df = pd.read_csv('transferencias - 05_2023.csv')

df = df.drop(columns=["ANO / MÊS"])
df['VALOR TRANSFERIDO'] = df['VALOR TRANSFERIDO'].str.replace(',', '.')
df["VALOR TRANSFERIDO"]= df["VALOR TRANSFERIDO"].astype('float')
print(df)