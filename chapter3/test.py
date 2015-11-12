import trees
myDat, labels = trees.createDataSet()
#print myDat
#print trees.createTree(myDat, labels)

import treePlotter
#treePlotter.createPlot()
#myTree = treePlotter.retrieveTree(0)
#treePlotter.createPlot(myTree)
#print trees.classify(myTree, labels, [1,1])

#trees.storeTree(myTree,'classifierStorage.txt')
#print trees.grabTree('classifierStorage.txt')

fr = open('lenses.txt')
print fr

lenses = [inst.strip().split('\t') for inst in fr.readlines()]
print lenses
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
print lensesTree
treePlotter.createPlot(lensesTree)