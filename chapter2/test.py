import kNN
group, labels = kNN.createDataSet()
#print kNN.classify0([0,0], group, labels, 3)
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
print datingDataMat[0:20]
print datingLabels[0:20]