import string
import os

def loadFileNames(part,isPositive):
    partString = "part" + str(part)
    groupString = "neg"
    if isPositive:
        groupString = "pos"

    cwd = os.getcwd()
    fileList = list(os.listdir(cwd + "/movie_review_dataset/" + partString + "/" + groupString))

    return fileList

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

def cleanReview(review, stopwords):
    #Transforma tudo em maiuscula
    uppercaseReview = review.upper()
    #remove pontuacao
    uppercaseReview = "".join(l for l in uppercaseReview if l not in string.punctuation)
    #cria set com palavras da review
    reviewWords = uppercaseReview.split()

    #remove stopwords dessa lista
    cleanWords = set([])
    for word in reviewWords:
        if word not in stopwords:
            cleanWords.add(word)

    return cleanWords

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