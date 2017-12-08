import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


from scipy import sparse, io


Xtreino = pd.read_csv('treino.csv')
Xteste = pd.read_csv('teste.csv')

#print Xtreino.head()
countvec = CountVectorizer(stop_words = 'english', ngram_range = (1,2), min_df = 2)

treino = countvec.fit_transform(Xtreino.Reviews) # Gera bag of words com palavras que ele nao viu antes

teste = countvec.transform(Xteste.Reviews)

# io.mmwrite("train.mtx", treino)
# io.mmwrite("test.mtx", teste)

knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(treino,Xtreino.Positive)

ypred = knn.predict(teste)

acc = accuracy_score(Xteste.Positive, ypred)
print acc