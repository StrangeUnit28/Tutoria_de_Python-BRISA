
## 1. Carregar o arquivo CSV

```
data = pd.read_csv('/content/Transferencias - 05_2023.csv')
```

## 2. Manipulação dos dados

```
data = data.drop(columns=['ANO / MÊS'])
data['VALOR TRANSFERIDO'] = data['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)
```

### Comprovando a substituição da vírgula

```
print(data['VALOR TRANSFERIDO'])
```

### Comprovando a alteração do tipo de dado

```
print(type(data['VALOR TRANSFERIDO'][0]))
``` 

## 3. Cálculos com NumPy

```
valor_maximo = np.max(data['VALOR TRANSFERIDO'])
valor_minimo = np.min(data['VALOR TRANSFERIDO'])
valor_medio = np.mean(data['VALOR TRANSFERIDO'])

print(f'Valor Máximo: {valor_maximo}')
print(f'Valor Mínimo: {valor_minimo}')
print(f'Valor Médio: {valor_medio}')
```

## 4. Visualização dos dados

#### Não deu tempo de fazer alterações estéticas no gráfico, mas o gabarito seria algo como:

```
tipos_favorecidos = data['TIPO FAVORECIDO'].unique()
valores_transferidos = data.groupby('TIPO FAVORECIDO')['VALOR TRANSFERIDO'].sum()

plt.bar(tipos_favorecidos, valores_transferidos)
plt.xlabel('Tipo Favorecido')
plt.ylabel('Valor Transferido')
plt.title('Valores Transferidos por Tipo Favorecido')
plt.show()
```