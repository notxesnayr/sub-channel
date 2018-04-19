import numpy as n
import scipy.integrate as s
def W3correlation(Pressure,XE,G,De,hi,hf,Qdprime,Actual_Multiplication_Factor,Len):
    K1 = n.zeros(100)
    K2 = n.zeros(100)
    K3 = n.zeros(100)
    K4 = n.zeros(100)
    K5 = n.zeros(100)
    CHFU = n.zeros(100)
    
    
    FRAC = Len/100
    
    CHF = n.zeros(100)
    

    integral2 = n.zeros(100)
    for z in range(0,100):
        #K1[z] = 3.1546*((2.022 - 0.06238*Pressure)+(0.1722 - 0.01427*Pressure)*n.exp((18.177-0.5987*Pressure)*XE[z]))
        #K2[z] = ((Gr)+1.037)*(0.109 - (1.173*XE[z]) + (0.127 * XE[z] * n.abs(XE[z])))
        #K3[z] = (1.157 - (0.869*XE[z]))
        #K4[z] = (0.2664 + (0.8357 * n.exp(-124.1*De)))
        #K5[z] = (0.8258 + (0.0000003413*((hf[z]*1000)-(hi[z]*1000))))
        K1[z] = (2.022 - (0.06238*Pressure)) + ((0.1722- (0.01427*Pressure))*n.exp(XE[z]*(18.177 - (0.5987*Pressure))))
        K2[z] = ((2.326*G) + 3271)*(0.1484 - (1.596*XE[z]) + (0.1729*XE[z]*n.abs(XE[z])))
        K3[z] = 1.157 - (0.869*XE[z])
        K4[z] = 0.2664 + (0.8357*n.exp(-124.1*De))
        K5[z] = 0.8258 + (0.0003413 * (hf[z] - hi[z]))
        CHFU[z] = K1[z]*K2[z]*K3[z]*K4[z]*K5[z]
    CHF = n.zeros(100)   
    F = n.zeros(100)
    C = n.zeros(100)
    for z in range(0,100):
        C[z] = 185.6*(((1-XE[z])**4.31)/(G**0.478))
        def integrand(x):
            if x == 0:
                return 0
            else:    
                return (Qdprime[int(x/FRAC)]*n.exp(-C[z]*(((z)*FRAC)-x)))
        (integral2[z], err) = s.quad(integrand, 0, (z*FRAC))
   
        F[z] = (C[z] * integral2[z]) / (Qdprime[z]*(1 - n.exp(-(C[z]*(z)*FRAC))))
    
        CHF[z] = CHFU[z] / F[z]
    return (CHF,CHFU,C,F)