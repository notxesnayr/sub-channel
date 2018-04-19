import numpy as n
import matplotlib.pyplot as plt
def kUO2(T,Burnup,FDR):
    if isinstance(T, int) or isinstance(T, n.float64):
        x = 1
        KUO2 = 0
    else:
        x = len(T)
        #print(x)
        TT = n.zeros(x)
        KUO2 = n.zeros((x,len(Burnup)))
    TT = T/1000
    if x != 1:
        
        for z in range(x):
            #print(z)
            First = (100 / (7.5408 + (17.692*TT[z]) + (3.6142 * (TT[z]**2))))        
            Second = (6400 / (TT[z]**2.5)) * n.exp(-16.35/TT[z])
            KUO2[z,0] = First + Second
        for i in range(1,len(Burnup)):
            for z in range(x):
            
                First = ((0.1148 + (0.0035*Burnup[i]) + (2.475*(10**-4)*(1-(0.003*Burnup[i])))*(T[z]-273.15))**-1) 
                Second = 0.0132 * (n.exp(0.00188*(T[z]-273.15)))
                KUO2[z,i] = First + Second
            
    else:  
    
                   
            if Burnup == 0:    
                First = (100 / (7.5408 + (17.692*TT) + (3.6142 * (TT**2))))        
                Second = (6400 / (TT**2.5)) * n.exp(-16.35/TT)
                KUO2 = First + Second
            else:
                First = ((0.1148 + (0.0035*Burnup) + (2.475*(10**-4)*(1-(0.003*Burnup)))*(T-273.15))**-1) 
                Second = 0.0132 * (n.exp(0.00188*(T-273.15)))
                KUO2 = First + Second
  
    if x!=1:
        KUO21=n.zeros((x,len(Burnup)))
        KUO21[:,:] = KUO2[:,:]
    if x ==1:
        KUO21 = KUO2

    return (KUO21)
T = n.linspace(300,3000,2701)
Burnup = [0.000E0,1.203E-2,2.406E-2,4.010E-2,2.406E-1,8.22E-1,1.444E0,2.406E0,3.609E0,7.058E0,1.607E1,1.428E1,1.789E1,2.150E1,2.510E1,2.871E1,3.232E1,3.593E1,3.954E1,4.391E1]
KUO2 = kUO2(T,Burnup,FDR)
colors = ['r','g','y','b','m','coral','c','k','darkblue','gold','khaki','maroon','orange','tan','crimson','cornsilk','lime','navy','pink','olive']
fig1 = plt.figure()
fig = fig1.add_subplot(111)
for i in range(20):
    fig = plt.plot(T,KUO2[:,i],colors[i],label=str(FDR[i])+'days')
leg = fig1.legend(loc='best')
plt.title("Thermal Conductivity of Uranium Dioxide",fontsize=20)
plt.xlabel('Temperature (K)',fontsize=15)
plt.ylabel(r'Thermal Conductivity $(\frac{W}{mK})$',fontsize=15)
