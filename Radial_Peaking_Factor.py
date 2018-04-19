import numpy as n
def Radial_Peaking_Factor(Tally14,Tally24,Tally34,Tally44,FDR):
    
    TOTAL = n.zeros(len(FDR))
    Average = n.zeros(len(FDR))
    MAX1 = n.zeros(len(FDR))
    MAX2 = n.zeros(len(FDR))
    MAX3 = n.zeros(len(FDR))
    MAX4 = n.zeros(len(FDR))
    MAX = n.zeros(len(FDR))
    RPF = n.zeros(len(FDR))
    ADD1 = n.sum(Tally14,axis=0)
    ADD2 = n.sum(Tally24,axis=0)
    ADD3 = n.sum(Tally34,axis=0)
    ADD4 = n.sum(Tally44,axis=0)
    long_list = []
    average_assembly = n.zeros(len(FDR))
    index = n.zeros(len(FDR))
    (M,burnup) = Tally14.shape
    (mm,burnup) = Tally24.shape
    (mmm,burnup) = Tally34.shape
    (mmmm,burnup) = Tally44.shape
    for c in range(M):
        for d in range(burnup):
            long_list.append(Tally14[c,d])
    for c in range(mm):
        for d in range(len(FDR)):
            long_list.append(Tally24[c,d])
    for c in range(mmm):
        for d in range(len(FDR)):
            long_list.append(Tally34[c,d])
    for c in range(mmmm):
        for d in range(len(FDR)):
            long_list.append(Tally44[c,d])
    for i in range(len(FDR)):
         TOTAL[i] = ADD1[i] + ADD2[i] + ADD3[i] + ADD4[i]
         Average[i] = TOTAL[i] / (49+4+52+52)
         MAX1[i] = n.nanmax(Tally14[:,i])
         MAX2[i] = n.nanmax(Tally24[:,i])
         MAX3[i] = n.nanmax(Tally34[:,i])
         MAX4[i] = n.nanmax(Tally44[:,i])
         MAX[i] = max(MAX1[i],MAX2[i],MAX3[i],MAX4[i])
         RPF[i] = MAX[i]/Average[i]
         average_assembly[i] = find_nearest(long_list,Average[i])
    
    
    return RPF,index,average_assembly,long_list,MAX,TOTAL,MAX1
