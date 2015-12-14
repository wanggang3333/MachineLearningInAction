import adaboost
from numpy import *

datMat, classLabels = adaboost.loadSimpData()
#D = mat(ones((5,1))/5)
#print adaboost.buildStump(datMat, classLabels, D)
#classifierArray = adaboost.adaBoostTrainDS(datMat, classLabels, 9)
#print classifierArray
dataArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray, aggClassEst = adaboost.adaBoostTrainDS(dataArr, labelArr, 10)
#testArr, testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
#prediction10 = adaboost.adaClassify(testArr, classifierArray)
#errArr = mat(ones((67,1)))
#print errArr[prediction10!= mat(testLabelArr).T].sum()
adaboost.plotROC(aggClassEst.T, labelArr)