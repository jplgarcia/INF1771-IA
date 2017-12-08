from sklearn import tree
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from scipy import  io

treino = io.mmread("train.mtx")

teste = io.mmread("test.mtx")

Xtreino = pd.read_csv('treino.csv')
Xteste = pd.read_csv('teste.csv')
Xtreino = pd.read_csv('treino.csv')
Xteste = pd.read_csv('teste.csv')

#print Xtreino.head()
countvec = CountVectorizer(stop_words = 'english', ngram_range = (1,2), min_df = 2)

treino = countvec.fit_transform(Xtreino.Reviews) # Gera bag of words com palavras que ele nao viu antes

teste = countvec.transform(Xteste.Reviews)


file = open("resultados.txt", "a")
clf = tree.DecisionTreeClassifier()
clf = clf.fit(treino, Xtreino.Positive)

ypred = clf.predict(teste)

acc = accuracy_score(Xteste.Positive, ypred)
acc = str(acc)
print "Resultado: - " + acc
resultado = "\nCLF: - " + acc
file.write(resultado)
file.close()