from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = datasets.load_breast_cancer()

# todos os atributos que o dataset contem
print("Dataset Keys: ", data.keys())

# O nome das features presentes no objeto
# Na literatura em português as features são chamadas de caracteristicas
print("Feature names: ", data['feature_names'])

# O nome da caracteristica que estamos interessados em classificar
# Na literatura em português target é chamado de rótulo
print("Target names: ", data['target_names'])

# Em uma pespectiva matemática, as features são os valores de x e os tagets são os valores de y.
# Portanto, por convenção, iremos usar X para armazenas os valores dentro de data['data'], pois é
# esse campo que guarda todos valores das features. E y receberá os valores de data['target]
X = data['data']
y = data['target']

# Porém devemos dividir o dataset entre dados que serão usados para treinar o modelo e os dados
# que serão usados para testar a eficácia do mesmo.
# Na linha abaixo o 0.2 representa a porcentagem dos dados que serão usados para testar o algoritmo
# ou seja 0.2 = 20%, portanto, 80% dos dados vão treinar o modelo e 20% servira como teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# clf é um acrônimo para classifier, ou seja, é o objeto que será responsável pela classificação
# SVC é uma sigla para Support Vector Machine. Esse é o algoritmo de aprendizado de máquina
# supervisionado que será usado para treinar o modelo. 
clf = SVC()
clf.fit(X_train, y_train)

# Aqui estamos conferindo a eficácia do modelo com os dados separados para teste
print(clf.score(X_test, y_test))
