import pandas as pd      
import matplotlib.pyplot as plt  
import numpy as np
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split

filmes = pd.read_csv("dados.csv")

amostra = filmes.sample(n=200)
x = amostra['Investimento (em milhoes)']
y = amostra['Bilheteria (pessoas)']
#visualizacao de dados
plt.scatter(x, y)
plt.show()

filmes_investimento = filmes['Investimento (em milhoes)']
filmes_bilheteria = filmes['Bilheteria (pessoas)']
treino, teste, treino_marcacoes, teste_marcacoes =  train_test_split(filmes_investimento, filmes_bilheteria)
treino = np.array(treino).reshape(len(treino), 1)
teste = np.array(teste).reshape(len(teste), 1)
modelo = LinearRegression()
modelo.fit(treino,treino_marcacoes)