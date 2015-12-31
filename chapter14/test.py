from numpy import *
import svdRec

# Data = svdRec.loadExData()
# U, Sigma, VT = linalg.svd(Data)
# Sig3 = mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[2]]])
# print U[:,:3] * Sig3 * VT[:3,:]

# myDat = mat(svdRec.loadExData())
# print svdRec.eulidSim(myDat[:,0],myDat[:,4])

# myDat = mat(svdRec.loadExData2())
# print svdRec.recommend(myDat, 1, estMethod = svdRec.svdEst)

svdRec.imgCompress(2)