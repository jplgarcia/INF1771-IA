import preprocess as pp

#Create negative reviews list
negativeReviews = pp.loadCleanReviewList(1,False)

#Create positive reviews list
positiveReviews = pp.loadCleanReviewList(1,True)

#set de palavras negativas
negativeWords = pp.createSetOfWords(negativeReviews)

#set de palavras positivas
positiveWords = pp.createSetOfWords(positiveReviews)

print len(negativeWords)
print len(positiveWords)

#sets de palavras boas/mas exclusivas remove a interseccao
(exclusivePositiveSet, exclusiveNegativeSet) = pp.makeExclusiveWordSets(positiveWords,negativeWords)

print len(exclusiveNegativeSet)
print len(exclusivePositiveSet)

#funcao de distancia
test = "Story of a man who has unnatural feelings for a pig. Starts out with a opening scene that is a terrific example of absurd comedy. A formal orchestra audience is turned into an insane, violent mob by the crazy chantings of it's singers. Unfortunately it stays absurd the WHOLE time with no general narrative eventually making it just too off putting. Even those from the era should be turned off. The cryptic dialogue would make Shakespeare seem easy to a third grader. On a technical level it's better than you might think with some good cinematography by future great Vilmos Zsigmond. Future stars Sally Kirkland and Frederic Forrest can be seen briefly."
cleanedReview = pp.cleanReview(test, pp.loadStopwords())

def calculateDistance(reviewSet, comparingSet):
    distance = 0
    for word in reviewSet:
        if word not in comparingSet:
            distance += 1
    return distance

def calculateBestNeighbours(reviewSet, positiveReviews, negativeReviews):
    positiveDistances = []
    negativeDistances = []
    for negativeReview in negativeReviews:
        distance = 0
        for word in reviewSet:
            if word not in negativeReview:
                distance += 1
        negativeDistances.append(distance)
    for positiveReview in positiveReviews:
        distance = 0
        for word in reviewSet:
            if word not in positiveReview:
                distance += 1
        positiveDistances.append(distance)

    positiveDistances.sort()
    negativeDistances.sort()
    print positiveDistances
    print negativeDistances

calculateBestNeighbours(cleanedReview, positiveReviews, negativeReviews)