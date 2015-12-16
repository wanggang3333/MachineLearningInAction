import regression
from numpy import *
import matplotlib.pyplot as plt

# xArr, yArr = regression.loadDataSet('ex0.txt')
# yHat = regression.lwlrTest(xArr,xArr,yArr,0.01)
# print yHat
# xMat = mat(xArr)
# srtInd = xMat[:,1].argsort(0)
# xSort = xMat[srtInd][:,0,:]
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(xSort[:,1], yHat[srtInd])
# ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
# plt.show()

#################### baoyu nianling #############################

abX, abY = regression.loadDataSet('abalone.txt')
# yHat01 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],0.1)
# yHat02 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],1)
# yHat03 = regression.lwlrTest(abX[0:99],abX[0:99],abY[0:99],10)

# print regression.rssError(abY[0:99], yHat01.T)
# print regression.rssError(abY[0:99], yHat02.T)
# print regression.rssError(abY[0:99], yHat03.T)

#print regression.ridgeRegres(abX, abY, 1)


# ridgeWeights = regression.ridgeTest(abX, abY)
# print ridgeWeights

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(ridgeWeights)
# plt.show()

###################### lego #######################################
lgX = []; lgY =[]
regression.setDataCollect(lgX, lgY)
print lgX,lgY 