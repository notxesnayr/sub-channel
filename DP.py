import math as m
from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
def DP(Tavg,Density,VIS,Pitch,FROD,massfr,Le):
    FA = (Pitch**2)-((m.pi*(FROD**2))/4)
    De = 4*FA/(m.pi*FROD)
    Re = massfr*De/VIS
    f = 0.184*(Re**-0.2)
    DP = ((f * (massfr**2)/(2*De*Density))*(Le) + (Density*9.81*Le))
    return DP