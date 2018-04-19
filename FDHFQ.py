import numpy as n
from scipy.integrate import simps
def FDHFQ(Q0prime,Actual_Multiplication_Factor,Burnup,Q0primedangerous,Le):
    Qprime = n.zeros(401)
    Qprimed = n.zeros(401)
    avgQprime = 0
    Len = n.linspace(0,Le,401)
    for v in range(401):
        Qprime[v] = Q0prime*Actual_Multiplication_Factor[v]
        avgQprime += Qprime[v]
        Qprimed[v] = Q0primedangerous*Actual_Multiplication_Factor[v]
    G = n.polyfit(Len[:],Qprime[:],2)
    H = n.polyfit(Len[:],Qprimed[:],2)
    AverageQprime = avgQprime / (v+1)
    FQ = Q0prime/AverageQprime
    FQdan = Q0primedangerous/AverageQprime
    UFr = 2.6/FQ #Uncertanty factor to make FQ the same as a nominal AP1000 reactor
    UFdr = 2.6/FQdan
    A = simps(G)
    B = simps(H)
    FDH = B/A
    return FQ,FQdan,FDH,G,UFr,UFdr,FQ,FQdan