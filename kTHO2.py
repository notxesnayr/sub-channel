import numpy as n
from pyXSteam.XSteam import XSteam
import matplotlib.pyplot as plt
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
def kTHO2(T,Burnup):
    if isinstance(T, int) or isinstance(T, n.float64):
        x = 1
        KTHO2 = 0
        alpha = 0
    else:
        x = len(T)
        KTHO2 = n.zeros((x,len(Burnup)))
        alpha = n.zeros(len(T))
    SHFx = (300,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000,3050,3099)
    SHFy = (60,72,78,82,85,88,90,95,100,105,120,130,135,140)
    #BP = [0,0.01203,0.02406,0.0401,0.2406,0.8422,1.444,2.406,3.609,7.058,10.67,14.28,17.89,21.5,25.1,28.71,32.32,35.93,39.54,43.91]
    BPth = [0, 0.00393, 0.007861, 0.0131, 0.07861, 0.2751, 0.4716, 0.7861, 1.179, 2.306, 3.485, 4.664, 5.843, 7.022, 8.201, 9.38, 10.56, 11.74, 12.92, 14.35]
    A = n.polyfit(SHFx,SHFy,3)
    p = n.poly1d(A)
    Cp = p(T)/264.04
    massratio = [1,1,1,1,0.997,9.990E-01,9.982E-01,9.969E-01,9.953E-01,9.908E-01,9.860E-01,9.812E-01,9.765E-01,9.720E-01,9.674E-01,9.630E-01,9.584E-01,9.538E-01,9.491E-01,9.435E-01]
    if x != 1:
        for t in range(x):
            KTHO2[t,0] = ((0.0213) + ((0.0001597) * T[t]))**-1
            alpha[t] = ((-34191.1)+(561.28*T[t]))**-1
        for i in range(1,len(Burnup)):
            for t in range(x):
                KTHO2[t,i] = KTHO2[t,0] * massratio[i]    
        
    
        fig1 = plt.figure()
        fig1.suptitle('Thermal Properties of Thorium Dioxide',fontsize=20)
        ALPHA = alpha * (10**6)
        subchanel1111 = fig1.add_subplot(3,1,1)
        subchanel1111.plot(T,Cp)
        plt.title(r'Specific Heat ($C_{p}$)')
        plt.xlabel('Temperature(K)')
        plt.ylabel(r'Specific Heat $(\frac{J}{(g)(K)})$',fontsize=10)
        subchanel2222 = fig1.add_subplot(3,1,3)
        subchanel2222.plot(T,ALPHA)
        plt.title(r'Thermal Diffusivity $ (\alpha) $')
        plt.xlabel('Temperature(K)')
        plt.ylabel(r'Thermal Diffusivity $(\frac{m^2}{s})$ X $10^{-6}$',fontsize=10)   
    else:
        for x,y in zip(range(0,20),BPth[:]):
            if Burnup == y:
                #print(y)
                KTHO2 = massratio[x]*(((0.0213) + ((0.0001597) * T))**-1) 
                alpha = ((-34191.1)+(561.28*T))**-1
                
    
    return (KTHO2)
T = n.linspace(300,3000,2701)
Burnup = [0.000E0,1.203E-2,2.406E-2,4.010E-2,2.406E-1,8.22E-1,1.444E0,2.406E0,3.609E0,7.058E0,1.607E1,1.428E1,1.789E1,2.150E1,2.510E1,2.871E1,3.232E1,3.593E1,3.954E1,4.391E1]
KTHO2 = kTHO2(T,Burnup)
colors = ['r','g','y','b','m','coral','c','k','darkblue','gold','khaki','maroon','orange','tan','crimson','cornsilk','lime','navy','pink','olive']
fig1 = plt.figure()
fig = fig1.add_subplot(111)
for i in range(20):
    fig = plt.plot(T,KTHO2[:,i],colors[i],label=str(FDR[i])+'days')
leg = fig1.legend(loc='best')
plt.title("Thermal Conductivity of Thorium Dioxide",fontsize=20)
plt.xlabel('Temperature (K)',fontsize=15)
plt.ylabel(r'Thermal Conductivity $(\frac{W}{mK})$',fontsize=15)