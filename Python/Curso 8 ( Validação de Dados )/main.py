from acesso_cep import BuscaEndereco
import requests

cep = 12345678
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

r = requests.get("https://viacep.com.br/ws/23015160/json/")
print(r.text)