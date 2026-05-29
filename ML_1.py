from dataclasses import dataclass

import pandas as pd

IOWA_FILE_PATH = 'C:/codigos/python/Machine Learning/data/test_iowa_data.csv' 

iowa_data = pd.read_csv(IOWA_FILE_PATH) # Lê o arquivo CSV e armazena os dados em um DataFrame do pandas

iowa_data.describe()

csv_data = iowa_data.describe()

print(iowa_data.describe(), "\n")

csv_data.to_csv('C:/codigos/python/Machine Learning/data/iowa_data.csv',)

print("Csv file created successfully.")
####################################################################################################################################################

oldest_house = 2026 - int(iowa_data['YearBuilt'].min())

print(f"The oldest house is {oldest_house} years old.")

oldest_year = 999999

for year in iowa_data['YearBuilt']:

    if year < oldest_year:
        oldest_year = year

oldest_house_age = 2026 - oldest_year

print(f"The oldest house is {oldest_house_age} years old.")

#################################################################################################################################################################

print(iowa_data.columns) # mostra as colunas do datase


