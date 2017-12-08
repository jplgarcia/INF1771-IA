import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from scipy import sparse, io

treino = io.mmread("train.mtx")

teste = io.mmread("test.mtx")

Xtreino = pd.read_csv('treino.csv')
Xteste = pd.read_csv('teste.csv')

knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(treino,Xtreino.Positive)

ypred = knn.predict(teste)

acc = accuracy_score(Xteste.Positive, ypred)
print acc
