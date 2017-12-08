import string
import os
import pandas as pd

# Description: Carrega os nomes das reviews contidos numa pagina
# param: part: 1 para conjunto de treino, 2 para conjunto teste
# param: isPositive: True se eh do conjunto positivo ou False do negativo
# returns: lista contendo strings de nomes dos arquivos
def loadFileNames(part,isPositive):
    partString = "part" + str(part)
    groupString = "neg"
    if isPositive:
        groupString = "pos"

    cwd = os.getcwd()
    fileList = list(os.listdir(cwd + "/movie_review_dataset/" + partString + "/" + groupString))

    return fileList

#carrega lista de stopwords
def loadStopwords():
    #abre arquivos de stopwords
    cwd = os.getcwd()
    file = open(cwd+"/stopwords.txt")
    stopwordsSet = set([])
    #para cada palavra adiciona ao set de stopwords
    for line in file:
        line = line.strip().upper()
        stopwordsSet.add(line)

    return stopwordsSet

# Description: Carrega uma review e remove quebra de linhas por paragrafos
# param: part: 1 para conjunto de treino, 2 para conjunto teste
# param: isPositive: True se eh do conjunto positivo ou False do negativo
# param: filename: nome do arquivo contendo a review
# returns: texto corrido da review (string)
def loadReview(part, isPositive, filename):
    partString = "part" + str(part)
    groupString = "neg"
    if isPositive:
        groupString = "pos"

    cwd = os.getcwd()
    file = open(cwd + "/movie_review_dataset/"+partString+"/"+groupString+"/"+filename)
    fullreview = ""
    for line in file:
        fullreview += (line + " ")

    return fullreview

# Description: Load review list and postive or negative list
# part 1 = train 2 = test
# Returns (reviewList, negpos)
# reviewList: contains the text of the reviews
# negpos: contaisn a list o the same size as the reviewList
# with True if the respective review is positive or False if it is negative
def loadReviewList(part):
    print "Loading file names..."
    posFileList = loadFileNames(part, True) # Get positive reviews from part 1
    negFileList = loadFileNames(part, False) # Get negative reviews from part 1
    print "File names loaded!"

    reviewList = []
    negpos=[] #True positive False Negative
    value = 0
    for name in posFileList:
        review = loadReview(part, True, name)
        reviewList.append(review)
        negpos.append(True)
        value += 1
    print "Numero de review positivas carregadas: " + str(value)
    value = 0
    for name in negFileList:
        review = loadReview(part, False, name)
        reviewList.append(review)
        negpos.append(False)
        value += 1
    print "Numero de review negativas carregadas: " + str(value)

    return (reviewList, negpos)

#remove stop words e coloca review em uppercase e transforma num array
def cleanReview(review, stopwords):
    #Transforma tudo em maiuscula
    uppercaseReview = review.upper()
    #remove pontuacao
    uppercaseReview = "".join(l for l in uppercaseReview if l not in string.punctuation)
    #cria set com palavras da review
    reviewWords = uppercaseReview.split()

    #remove stopwords dessa lista
    cleanWords = []
    for word in reviewWords:
        if word not in stopwords:
            cleanWords.add(word)

    return cleanWords

#cria um set a partir de uma lista
def setFromList(wordsList):
    wordSet = set([])
    for word in wordsList:
        wordSet.add(word)

#carrega a lista de reviews
def loadCleanReviewList(part, isPositive):
    print "Loading file names..."
    fileList = loadFileNames(part, isPositive)
    print "File names loaded!"
    print "Loading stopwords"
    stopwords = loadStopwords()
    print "Stopwords loaded!"

    numOfFiles = len(fileList)
    currentFile = 0.0
    reviewList = []
    for name in fileList:
        percentage = float((currentFile+1)/numOfFiles * 100.0)
        review = loadReview(part,isPositive, name)
        cleanedReview = cleanReview(review, stopwords)
        reviewList.append(cleanedReview)
        print (str(percentage) + "% :::::: Review: " + name + " Added to set!")
        currentFile = currentFile + 1
    return reviewList

#Cria uma lista de palavras positivas apartir de um conjunto de reviews
def createSetOfWords(setOfReviews):
    wordSet = set([])
    for subset in setOfReviews:
        for word in subset:
            wordSet.add(word)
    return wordSet

#Criar dois sets de palavras apenas exclusivas a partir de dois sets de palavras nao exclusivas
def makeExclusiveWordSets(positiveSet, negativeSet):
    newPositiveSet = set(positiveSet)
    newNegativeSet = set(negativeSet)
    for word in positiveSet:
        if word in negativeSet:
            newNegativeSet.remove(word)
            newPositiveSet.remove(word)

    return(newPositiveSet, newNegativeSet)

(reviewList, isPositiveList) = loadReviewList(1)
(reviewListTest, isPositiveListTest) = loadReviewList(2)

print "Numero total de reviews carregadas: " + str(len(reviewList))
Xtreino = pd.DataFrame()
Xteste = pd.DataFrame()

Xtreino['Reviews'] = pd.Series(reviewList)
Xtreino['Positive'] = pd.Series(isPositiveList)

Xteste['Reviews'] = pd.Series(reviewListTest)
Xteste['Positive'] = pd.Series(isPositiveListTest)

Xteste.to_csv('teste.csv', index = False)
Xtreino.to_csv('treino.csv', index = False)