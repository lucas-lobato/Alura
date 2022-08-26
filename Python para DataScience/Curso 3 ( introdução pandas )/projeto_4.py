import pandas as pd

dados = pd.read_csv('db.csv', sep=';', index_col=0)
print('\n************************ TODOS OS DADOS ****************************')
print(dados) # Mostra todos os dados
print('\n************************ DADOS INICIAIS ****************************')
print(dados.head())
print('\n******************* DADOS PELA CARACTERISTICA **********************')
loc = dados.loc[['Passat','DS5'],['Motor','Valor']]
print(loc) # Mostra apenas os carros desejados pelo nome e mostra as caracteristicas pelo nome
print('\n****************** DADOS PELO INDICE *******************************')
iloc = dados.iloc[7:10]
print(iloc) # Mostra as informaçoes pelo indice
print('\n****************** DADOS PELA VARIAVEL *****************************')
print(dados[(dados.Motor == 'Motor Diesel') & (dados.Zero_km == True)]) # Mostra as informações pela variavel
print('\n****************** DADOS PELA VARIAVEL *****************************')
print(dados.query('Motor == "Motor Diesel" and Zero_km == True')) # Mostra as informações pela variavel
print('\n****************** DADOS TRATADOS **********************************')
dados.fillna(0, inplace= True) # Substirui todos os valores nulos por 0
print(dados)
print('\n****************** DADOS TRATADOS **********************************')
dados.dropna(subset= ['Quilometragem'], inplace= True) # Apaga os valores nulos da coluna desejada
print(dados)
print('\n****************** DADOS TRATADOS **********************************')