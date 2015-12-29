import apriori
dataSet = apriori.loadDataSet()
# print dataSet
# C1 = apriori.createC1(dataSet)
# print C1
# D = map(set,dataSet)
# print D

# L1, supportData0 = apriori.scanD(D, C1, 0.5)
# print L1

# L, supportData = apriori.apriori(dataSet,minSupport = 0.5)
# rules = apriori.generateRules(L,supportData,minConf = 0.5)
# print rules  


# mushroom test
mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
L, supportData = apriori.apriori(dataSet,minSupport = 0.3)

for item in L[1]:
	if item.intersection('2'): print item