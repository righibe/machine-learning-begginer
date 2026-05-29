from sklearn.tree import DecisionTreeRegressor
import pandas as pd 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

iowa_file_path = 'C:/codigos/python/Machine Learning/data/train_iowa_data.csv'

iowa_data = pd.read_csv(iowa_file_path)

iowa_data_filtrado = iowa_data.dropna(axis=0)

print(iowa_data.columns, "\n")

iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data_filtrado[iowa_features]

y = iowa_data_filtrado.SalePrice

iowa_model = DecisionTreeRegressor(random_state=42)

iowa_model.fit(X, y)

predictions = iowa_model.predict(X)

predicted_home_prices = iowa_model.predict(X)

mean_absolute_error(y, predicted_home_prices)