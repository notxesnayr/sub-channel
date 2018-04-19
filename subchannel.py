'''This code will take an MCNP run file (I am using Uranium Dioxide and Thorium Dioxide) and will find 
the thermodynamic properties of a nominal AP1000 reactor'''
import matplotlib
import numpy as n
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
import warnings
warnings.filterwarnings("ignore")
#ASSUMPTIONS
T_inlet = 553 #K
ko = 2E-3 #Oxide heat conduction coefficient (kW/mK)
kc = 0.01385 #(kW/m*K)
Len = 4.2672 #Core height cold active fuel (m)
FRAC = Len/100 #making 1000 index into length
dRf = 0.003 #delta R or L (m)
Le = Len + 2*dRf #Length equivalent
Rf = 0.00409575 #(m) Radius of Fuel (NEEDS TO BE CHANGED ONCE THORIUM)
RUO2 = 0.00409575
RThO2 = 'null'
FRACr = Rf/100 #making 100 index into radius
Rg = 0.00426085 #Outer Radius of gap (m)
Rci = Rg #Inner Radius of clad is outer radius of gap
Rco = Rci + 0.0005715 #Outer Radius of Cladding (m)
Roo = 0.00488235 #Outer Radius of Oxide (m)
dc = (Rco - Rci) #Thickness of Cladding (m)
do = 0.05/1000 #Thickness of Oxide (m)
Tavg = 576.5388888 #Average Temperature of the core (K)
Density = 704.88#(NEEDS TO BE  CHANGED?)
VIS = 84.6E-6 #(NEEDS TO BE CHANGED?)
Q0prime = 48.8845144 #(kW/m) max linear heat rate
Q0primedangerous = 73.6548556
GTotal = 13456.57 #Total mass flow rate(kg/s)
Pitch = 0.0125984 #(m)
FROD =0.0094996 #Fuel Rod Outside Diameter (m)
h = 34  #kW/mK (Clad-Coolant)
hgap = 5.7  #kW/mK
SFA = (Pitch**2) - ((n.pi/4)*FROD**2) #(m^2)
massfr = (GTotal/41448) #(Mass Flow Rate per rod (kg/s))
massfrpr = massfr/SFA #(Mass Velocity (kg/s*m^2))
Te = n.linspace(300,3100,2801) #K
Pw  = (n.pi * FROD) #m
Dh = (4/n.pi)*(SFA/FROD)
Pressure = 15.5132
DNBR = n.zeros(100)
Cells14,Cells24,Cells34,Cells44,Tally34lol,Tally44lol,Tally24lol,Tally14lol,APD,RRD1,FDR,Y,YY,YYY,YYYY,Actual_Multiplication_Factor,Burnup,PFAPD = look()
RPF,index,average_assembly,long_list,MAX,TOTAL,MAX1  =  Radial_Peaking_Factor(Y,YY,YYY,YYYY,FDR)
P0 = DP(Tavg,Density,VIS,Pitch,FROD,massfrpr,Le)
(TMOD,enthalpy_liquid,enthalpy_actual,Specific_Heat,integral999,now,AAA) = Tmod(T_inlet,Q0prime,Actual_Multiplication_Factor,Le,Len,massfr,Pitch,FROD,Pressure)
print(n.nanmax(TMOD))
(TCO, ZMAX1, MAXTEMPO, zmax1, TCI, ZMAX3, MAXTEMPI, Qdprime) = Tco(T_inlet,Q0prime,Actual_Multiplication_Factor,integral999,massfr,Le,Len,Rco,Specific_Heat,FROD,Dh)
print(n.nanmax(TCI))
(KTHO2) = kTHO2(Te,Burnup)
(KUO2) = kUO2(Te,Burnup)
(TFCLarray, T, ZMAXXXX , BurnupStep, know,J0 , Sixth) = Tfcl(Burnup,T_inlet,Q0prime,Actual_Multiplication_Factor,integral999,massfr,Specific_Heat,Le,FRAC,Rco,Rci,Roo,Rg,hgap,h,ko,kc,do,FRACr,Rf,dRf)
(XE, hfg, hgas) = Xe(TMOD,Pressure,enthalpy_actual,enthalpy_liquid,Q0prime,Actual_Multiplication_Factor,Le,massfr,Specific_Heat)
(CHF,CHFU,C,F) = W3correlation(Pressure,XE,massfrpr,Dh,enthalpy_actual,enthalpy_liquid,Qdprime[:],Actual_Multiplication_Factor,Len)
FQ,FQdan,FDH,G,UFr,UFdr,FQr,FQdanr = FDHFQ(Q0prime,Actual_Multiplication_Factor,Burnup,Q0primedangerous,Len)
font={'size':8}
matplotlib.rc('font',**font)
fig2 = plt.figure()
plt.subplots_adjust(hspace=0.25)
fig2.suptitle('Axial Temperature Distributions', fontsize=20)
fig3 = plt.figure()
fig3.suptitle('Thermal Conductivity of Thorium Dioxide versus Temperature',fontsize=20)
plt.xlabel('Temperature (K)',fontsize=17)
plt.ylabel(r'Thermal Conductivity $(\frac{W}{mK})$',fontsize=17)
fig4 = plt.figure()
plt.title('Radial Temperature Distribution of the Fuel',fontsize=20)
plt.xlabel('Radius (mm)',fontsize=12)
plt.ylabel('Temperature(K)',fontsize=12)
F = n.array([str,str,str,str,str,str,str])
Q = n.zeros(7)
b = n.array([str,str,str,str,str,str,str])
for x,y in zip(range(0,6),[str(ZMAXXXX[0]*FRAC) + str(' max'),str(50*FRAC),str(35*FRAC),str(20*FRAC),str(15*FRAC),str(5*FRAC)]):
            b[x] = y
green_patch = mp.Patch(color='green',label=b[0])
yellow_patch = mp.Patch(color='yellow',label=b[1])  
orange_patch = mp.Patch(color='orange',label=b[2])    
blue_patch = mp.Patch(color='blue',label=b[3])
red_patch = mp.Patch(color='red',label=b[4])
black_patch = mp.Patch(color='black',label=b[5])


A = plt.legend(title='Height from the Bottom of the Core', handles=[green_patch,yellow_patch,orange_patch,blue_patch,red_patch,black_patch],loc='best')
A.FontSize = 6


DNBRU = n.zeros(100)
for z in range(0,100):
    DNBR[z] = (CHF[z] / Qdprime[z])
    DNBRU[z] = (CHFU[z] / Qdprime[z])
MDNBR = n.nanmin(DNBR[:])
MDNBRU = n.nanmin(DNBRU[:])
print('The MDNBR is',MDNBRU,'for a uniform heat flux')
print('The MDNBR is', MDNBR,'for a non-uniform heat flux')

L = n.linspace(0,Len,100)

f, (sub1,sub2,sub3) = plt.subplots(3,sharex=True)
f.suptitle('Axial Distributions of Various Properties',fontsize = 20)

d = ('Heat Flux','Critical Heat Flux (nonuniform)','Critical Heat Flux (uniform)')
blue_patch2 = mp.Patch(color='blue',label=d[0])
green_patch2 = mp.Patch(color='green',label=d[1])
red_patch = mp.Patch(color='red',label=d[2])
L2 = n.linspace(0,Len,100)
sub1.plot(L2[:],Qdprime[:],'b',L2[3:100],CHF[3:100],'g',L2[:],CHFU[:],'r')
sub1.legend(handles = [blue_patch2, green_patch2,red_patch])
sub1.set_ylabel(r'Heat Flux ($\frac{kW}{m^2}$)',fontsize=12)
sub1.set_title('Heat Flux')

sub2.plot(L2[:],enthalpy_liquid[:],'b',L2[:],enthalpy_actual[:],'g')
sub2.set_title('Enthalpy')
e = ("Enthalpy $T_{sat}$","Enthalpy Two-Phase Flow")
blue_patch3 = mp.Patch(color='blue',label=e[0])
green_patch3 = mp.Patch(color='green',label=e[1])
sub2.legend(handles = [blue_patch3, green_patch3])
sub2.set_ylabel(r'Enthalpy ($\frac{kW}{kJ}$)',fontsize=12)

sub3.plot(L2[:],XE[:])
sub3.set_title('Equilibrium Quality')
sub3.set_xlabel('Height (m)',fontsize=12)
sub3.set_ylabel('$X_E$',fontsize=12)
colors = ['r','g','y','b','m','coral','c','k','darkblue','gold','khaki','maroon','orange','tan','crimson','cornsilk','lime','navy','pink','olive']
subplot66 = fig3.add_subplot(1,1,1)
for i in range(len(FDR)):
    subplot66.plot(Te,KTHO2[:,i],colors[i],label=str(FDR[i])+'days')
leg = fig3.legend(loc='best')

colors = ['r','g','y','b','m','coral','c','k','darkblue','gold','khaki','maroon','orange','tan','crimson','cornsilk','lime','navy','pink','olive']
fig5 = plt.figure()
plt.title("Thermal Conductivity of Uranium Dioxide")
subplot9 = fig5.add_subplot(111)
for i in range(len(FDR)):
    subplot9.plot(Te[:],KUO2[:,i],colors[i],label=str(FDR[i])+' days')

leg = fig5.legend(loc='best')
plt.xlabel('Temperature (K)')
plt.ylabel(r'Thermal Conductivity $(\frac{W}{mK})$')
RR = n.linspace(0,Rf*1000,100)


subplot1 = fig2.add_subplot(2,2,1)
subplot1.plot(L2,TMOD)
subplot1.set_title('Bulk Temperature of the Moderator')
subplot1.set_ylabel('Temperature (K)')

subplot2 = fig2.add_subplot(2,2,3)
subplot2.plot(L2,TCO[:],'b',L2,TCI[:],'r')
subplot2.set_title('Temperature of the Cladding')
subplot2.set_xlabel('Height (m)')
subplot2.set_ylabel('Temperature (K)')
blue_p = mp.Patch(color='blue',label='Outer Cladding')
red_p = mp.Patch(color='red',label='Inner Cladding')
subplot2.legend(handles=[blue_p,red_p])


L1 = n.linspace(0,Len,100)
colors = ['r','g','y','b','m','coral','c','k','darkblue','gold','khaki','maroon','orange','tan','crimson','cornsilk','lime','navy','pink','olive']
L = n.linspace(0,Len,100)
subplot3 = fig2.add_subplot(1,2,2)
for d in range(0,len(FDR)):
    subplot3.plot(L[:],TFCLarray[0,:,d],colors[d],label=str(FDR[d])+'days')
leg1=subplot3.legend(loc='best')
subplot3.set_title('Temperature of the Centerline of Fuel')
subplot3.set_xlabel('Height (m)')
subplot3.set_ylabel('Temperature (K)')

subplot4 = fig4.add_subplot(111)

subplot4.plot(RR,TFCLarray[:,int(ZMAXXXX[0]),0],'g',RR,TFCLarray[:,35,0],'orange',RR,TFCLarray[:,20,0],'k',RR,TFCLarray[:,15,0],'r',RR,TFCLarray[:,50,0],'y',RR,TFCLarray[:,5,0],'b')

Azmax = n.zeros(len(Burnup))
for x in range(len(Burnup)):
    Azmax[x] = ZMAXXXX[x] * FRAC
    print('The maximum temperature of the fuel,',T[x], 'degrees Kelvin, is at',Azmax[x],'m at',Burnup[x],'GWd/MT burnup' )
print('The pressure drop along the subchannel is',P0,'Pa')
