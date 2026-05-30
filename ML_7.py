from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

iowa_path = 'C:/codigos/python/Machine Learning/data/train_iowa_data.csv'
iowa_data = pd.read_csv(iowa_path)

y = iowa_data.SalePrice

iowa_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = iowa_data[iowa_features]

# '''
# train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    # model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # model.fit(train_X, train_y)
    # preds_val = model.predict(val_X)
    # mae = mean_absolute_error(val_y, preds_val)
    # return mae
# '''
# erro = 1e10
# candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# for candidate in candidate_max_leaf_nodes:
    # erro_do_candidato = get_mae(candidate, train_X, val_X, train_y, val_y)
    # print(f"Max leaf nodes: {candidate}  MAE: {erro_do_candidato}\n")
    # if erro_do_candidato < erro:
        # erro = erro_do_candidato
        # best_tree_size = candidate

final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=2)
final_model.fit(X, y)

lotAreaNova = float(input("Digite o valor do LotArea: "))
yearBuiltNova = int(input("Digite o valor do YearBuilt: "))
firstFlrSFNova = int(input("Digite o valor do 1stFlrSF: "))
secondFlrSFNova = int(input("Digite o valor do 2ndFlrSF: "))
fullBathNova = int(input("Digite o valor do FullBath: "))
bedroomAbvGrNova = int(input("Digite o valor do BedroomAbvGr: "))
totRmsAbvGrdNova = int(input("Digite o valor do TotRmsAbvGrd: "))

nova_casa = pd.DataFrame({
    'LotArea': [lotAreaNova],
    'YearBuilt': [yearBuiltNova],
    '1stFlrSF': [firstFlrSFNova],
    '2ndFlrSF': [secondFlrSFNova],
    'FullBath': [fullBathNova],
    'BedroomAbvGr': [bedroomAbvGrNova],
    'TotRmsAbvGrd': [totRmsAbvGrdNova]
})

preco_nova_casa = final_model.predict(nova_casa)
print(f"O preço estimado para a nova casa é: {preco_nova_casa[0]}")


