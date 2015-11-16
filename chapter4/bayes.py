#coding:gbk
from numpy import *


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 代表侮辱性文字，0 代表正常言论
    return postingList,classVec
	
def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)
	
def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec
	
def bagOfwords2VecMN(vocabList, inputSet):
	returnVec = [0] * len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] += 1

	return returnVec
	
def trainNB0(trainMatrix, trainCategory):
	numTrainDocs = len(trainMatrix)
	numsWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs)
	p0Num = ones(numsWords)
	p1Num = ones(numsWords)
	p0Denom = 2.0
	p1Denom = 2.0
	for i in range(numTrainDocs):
		if trainCategory[i] == 0:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
		else:
			p1Num += trainMatrix[i]
			p1Denom  += sum(trainMatrix[i])
	p1Vect = log(p1Num / p1Denom)
	p0Vect = log(p0Num / p0Denom)
	return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec,p1Vec, pClass1):
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0
		
def testingNB():
	listOPosts, listClasses = loadDataSet()
	myVocabList = createVocabList(listOPosts)
	trainMat = []
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
	p0V, p1V, pAb = trainNB0(array(trainMat),array(listClasses))
	testEntry = ['love', 'my','dalmation']
	thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
	print testEntry,'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
	testEntry = ['stupid', 'garbage']
	thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
	print testEntry,'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
	
def textParse(bigString):
	import re
	listOfTokens = re.split(r'\W*',bigString)
	return [tok.lower for tok in listOfTokens if len(tok) > 2]

def spamTest():
	docList = []; classList = []; fullText = []
	for i in range(1,26):
		wordList = textParse(open('email/spam/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(open('email/ham/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)
	trainingSet = range(50); testSet = []
	for i in range(10):
		randIndex = int(random.uniform(0, len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []; trainClasses = []
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
	
	errorCount = 0

	print testSet
	for docIndex in testSet:
		wordVector = setOfWords2Vec(vocabList, docList[docIndex])
		if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			print 'error :',docIndex,classifyNB(array(wordVector), p0V, p1V, pSpam),classList[docIndex]
			errorCount += 1			
	print 'the error rate is : ', float(errorCount)/len(testSet)
	
def calcMostFreq(vocabList, fullText):
	import operator
	freqDict = {}
	for token in vocabList:
		freqDict[token] = fullText.count(token)
	sortedFreq = sorted(freqDict.iteritems(),key = operator.itemgetter(1),reverse = True)
	return sortedFreq[:30]
	
def localWords(feed1, feed0):
	import feedparser
	docList = []
	classList = []
	fullText = []
	minLen  = min(len(feed1['entries']),len(feed0['entries']))
	for i in range(minLen):
		wordList = textParse(feed1['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList = textParse(feed0['entries'][i]['summary'])
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList = createVocabList(docList)
	top30Words = calcMostFreq(vocabList, fullText)
	for pairW in top30Words:
		if pairW[0] in vocabList: vocabList.remove(pairW[0])
	trainingSet = range(2 * minLen); testSet = []
	for i in range(20):
		randIndex = int(random.uniform(0,len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat = []; trainClasses = []
	for docIndex in trainingSet:
		trainMat.append(bagOfwords2VecMN(vocabList, docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V,p1V, pSpam = trainNB0(array(trainMat),array(trainClasses))
	errorCount = 0
	for docIndex in testSet:
		wordVector = bagOfwords2VecMN(vocabList, docList[docIndex])
		if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
			errorCount += 1
	print 'the error rate is : ', float(errorCount)/ len(testSet)
	return vocabList, p0V, p1V
	
def getTopWords(ny, sf):
	import operator
	vocabList, p0V, p1V = localWords(ny, sf)
	print vocabList[:30]
	print p0V[:30]
	topNY = []; topSF = [];
	for i in range(len(p0V)):
		if p0V[i] > -6.0: topSF.append((vocabList[i],p0V[i]))
		if p1V[i] > -6.0: topNY.append((vocabList[i],p1V[i]))
	sortedSF = sorted(topSF, key = lambda pair: pair[1], reverse = True)
	# print 'SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**'
	# for item in sortedSF:
		# print item[0]
	# sortedNY = sorted(topNY, key = lambda pair: pair[1], reverse = True)
	# print 'NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**'
	# for item in sortedNY:
		# print item[0]
			
		
		

	
		
		
	
