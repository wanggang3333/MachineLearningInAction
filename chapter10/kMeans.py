from numpy import *

def loadDataset(fileName):
	datamat = []
	fr = open(fileName)
	for line in fr.readlines():
		curLine = line.strip().split('\t')
		fltLine = map(float, curLine)
		dataMat.append(fltLine)
	return dataMat
	
def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA-vecB, 2)))
	
def randCent(dataMat, k):
	n = shape(dataMat)[1]
	centroids = mat(zeros((k,n)))
	for j in range(n):
		minJ = min(dataSet[:,j])
		rangeJ = float(max(dataSet[:,j]) - minJ)
		centroids[:,j] = minJ + rangeJ * random.rand(k,1)
	return centroids
	
