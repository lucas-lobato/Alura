import pandas as pd
#pd.set_option('display.max_rows', 300) -> ver 300 linhas
#pd.set_option('display.max_columns', 50) -> ver 50 colunas


dataset = pd.read_csv("db.csv", sep=';')
print(dataset)
print('\n****************************************\n')
print(dataset[['Quilometragem','Valor']].describe())
