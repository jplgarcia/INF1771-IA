import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
Xtreino = pd.read_csv('treino.csv')
Xteste = pd.read_csv('teste.csv')

countvec = CountVectorizer(stop_words = 'english', ngram_range = (1,2), min_df = 2)

treino = countvec.fit_transform(Xtreino.Reviews) # Gera bag of words com palavras que ele nao viu antes

teste = countvec.transform(Xteste.Reviews)

hls = (10,7,5,4)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=hls, random_state=1)
clf = clf.fit(treino, Xtreino.Positive)

file = open("resultados_neural_network.txt", "a")


ypred = clf.predict(teste)

acc = accuracy_score(Xteste.Positive, ypred)
acc = str(acc)
print "Resultado: - " + acc
resultado = "\nNeural Network: - " + acc + " hidden_layer_sizes=" + str(hls)
file.write(resultado)
file.close()