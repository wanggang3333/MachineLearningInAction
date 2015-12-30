import fpGrowth

# rootNode = fpGrowth.treeNode('pyramid', 9, None)
# rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
# rootNode.disp()

#simpDat = fpGrowth.loadSimpDat()
# print simpDat
#initSet = fpGrowth.createInitSet(simpDat)
#print initSet

#myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)

#freqItems = []

#fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)

#print freqItems

parsedDat = [line.split() for line in open('kosarak.dat').readlines()]
initSet = fpGrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 100000)
myFreqList = []
fpGrowth.mineTree(myFPtree, myHeaderTab, 100000, set([]), myFreqList)
print myFreqList