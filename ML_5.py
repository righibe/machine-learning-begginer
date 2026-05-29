from sklearn.tree import DecisionTreeRegressor
import pandas as pd #biblioteca usada
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

iowa_file_path = 'C:/codigos/python/Machine Learning/data/train_iowa_data.csv'
iowa_data = pd.read_csv(iowa_file_path) # Lê o arquivo CSV e armazena os dados em um DataFrame do pandas

y = iowa_data.SalePrice

iowa_data_filtrado = iowa_data.dropna(axis=0)

iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data[iowa_features]

iowa_model = DecisionTreeRegressor(random_state=42)

iowa_model.fit(X, y)

print(""""Até agora:
      
      - Carregamos os dados
      - Selecionamos as features
      - Treinamos o modelo
      
      """)
print("features: ", X.columns.tolist())
print("predicts: ", iowa_model.predict(X.head()))
print("predicts: ", y.head().tolist())
