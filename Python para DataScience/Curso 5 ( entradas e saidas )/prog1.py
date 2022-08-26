import pandas as pd
import numpy as np
import html5lib
import seaborn as sns


nomes_m = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=m")
nomes_f = pd.read_json("https://servicodados.ibge.gov.br/api/v1/censos/nomes/ranking?qtd=200&sexo=f")

frames = [nomes_f,nomes_m]
nomes = pd.concat(frames)['nome'].to_frame()

np.random.seed(123)
total_alunos = len(nomes)

nomes["id_aluno"] = np.random.permutation(total_alunos) + 1
dominios = ['@outlook.com','@gmail.com']

nomes['dominio'] = np.random.choice(dominios, total_alunos)
nomes['email'] = nomes.nome.str.cat(nomes.dominio).str.lower()

url = 'http://tabela-cursos.herokuapp.com/index.html'
cursos = pd.read_html(url)

cursos = cursos[0]
cursos = cursos.rename(columns={'Nome do curso' : 'nome_do_curso'})
cursos['id'] = cursos.index + 1
cursos = cursos.set_index('id')

nomes['matriculas'] = np.ceil(np.random.exponential(size=total_alunos) * 1.5).astype(int)

print(nomes)

print(sns.distplot(nomes.matriculas))