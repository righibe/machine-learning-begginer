from sklearn.tree import DecisionTreeRegressor
import pandas as pd 

iowa_file_path = 'C:/codigos/python/Machine Learning/data/train_iowa_data.csv'

iowa_data = pd.read_csv(iowa_file_path)

print(iowa_data.columns, "\n")

iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data[iowa_features]

y = iowa_data.SalePrice

iowa_model = DecisionTreeRegressor(random_state=42)

iowa_model.fit(X, y)

predictions = iowa_model.predict(X)

print(X.describe(), "\n")

print(X.head(), "\n")

print(predictions, "\n")