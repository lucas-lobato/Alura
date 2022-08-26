import pandas

carros = ['Cross Fox','Aston Martins','Jetta']
valores = [13864, 131244314, 4124123]

dados = dict(zip(carros,valores))
print(dados)
print('\n',sum(dados.values()))
