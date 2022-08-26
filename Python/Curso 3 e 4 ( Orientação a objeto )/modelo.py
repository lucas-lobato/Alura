class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return "Nome:{} - Ano:{} - Likes:{}".format(self._nome, self.ano, self._likes)


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Nome:{} - Ano:{} - Duração:{} - Likes:{}".format(self._nome, self.ano, self.duracao, self._likes)


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome:{} - Ano:{} - Temporadas:{} - Likes:{}".format(self._nome, self.ano, self.temporadas, self._likes)


class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores Guerra infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 120)
demolidor = Serie("demolidor", 2017, 5)

vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
fim_de_semana = PlayList("fim de semana", filmes_e_series)

for programa in fim_de_semana:
    print(programa)
