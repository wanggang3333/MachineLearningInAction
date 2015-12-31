import pca
import matplotlib
import matplotlib.pyplot as plt
# dataMat = pca.loadDataSet('testSet.txt')
# lowDat, reconMat = pca.pca(dataMat, 1)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(dataMat[:,0].flatten().A[0], dataMat[:,1].flatten().A[0], marker='^', s=90)
# ax.scatter(reconMat[:,0].flatten().A[0], reconMat[:,1].flatten().A[0], marker='o', s=50,c='red')

# plt.show()

dataMat = pca.replaceNanWithMean()
