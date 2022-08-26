import pandas as pd

dados = [
    {'Nome':'Jetta', 'Motor':'Motor 4.0', 'Ano':2004, 'Quilometragem': 12345.0, 'Zero_km': False, 'Valor': 15567.0},
    {'Nome':'Passat', 'Motor':'Motor 1.0', 'Ano':2018, 'Quilometragem': 6782345.0, 'Zero_km': False, 'Valor': 10967.0},
    {'Nome':'CrossFox', 'Motor':'Motor 2.0', 'Ano':2013, 'Quilometragem': 345345.0, 'Zero_km': False, 'Valor': 18567.0}
]

dataset = pd.DataFrame(dados)
print(dataset)