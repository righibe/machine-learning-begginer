import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = 'C:/codigos/python/Machine Learning/data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 


melbourne_data.columns # pega as coluhnas

melbourne_data = melbourne_data.dropna(axis=0) # remove as linhas com valores ausentes

y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]

X.describe()

X.head()

melbourne_model = DecisionTreeRegressor(random_state=1)# cria o modelo de regressão de árvore de decisão com uma semente aleatória para garantir a reprodutibilidade dos resultados

print(melbourne_model.fit(X, y))

print(X.head())

print(y.head().tolist())

