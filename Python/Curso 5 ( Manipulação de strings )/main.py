from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
argumentosUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaOrigem,moedaDestino,valor)

ExtratorArgumentosUrl.urlEhValida("a")

#padrao = "[0-9]{4,5}[-]*[0-9]{4,5}"