from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

path = 'C:/codigos/python/Machine Learning/data/train_iowa_data.csv'
iowa_data = pd.read_csv(path)
iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
iowa_features1 = iowa_data.select_dtypes(include=['int64', 'float64']).columns.drop('SalePrice') # Seleciona apenas as colunas numéricas, que diminui o MAE

y = iowa_data.SalePrice

X = iowa_data[iowa_features1]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

iowa_model = DecisionTreeRegressor()

iowa_model.fit(train_X, train_y)

val_predictions = iowa_model.predict(val_X.head())
values = val_y.head().tolist()

mae = mean_absolute_error(values, val_predictions)

print(val_predictions)
print(values)
print("MAE: ", mae)
