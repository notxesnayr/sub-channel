#Mistake enthalpy with heat transfer coefficient (MAYBE BECAUSE THEY HAVE THE SAME FUCKING SYMBOL)
from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
import numpy as n
def Xe(Tmod,P,enthalpy_actual,enthalpy_liquid,Q0prime,Actual_Multiplication_Factor,Le,G,Cp):
    hf = n.zeros(100)
    hi = n.zeros(100)
    Xe = n.zeros(100)
    FRAC = Le/100
    hgas = n.zeros(100)
    hfg = n.zeros(100)
    P = 15.5132
    for z in range(0,100):
        hf[z] = steamTable.hL_p(P)
        #hi[z] = steamTable.h_prho(P,Cp[z])
        hgas[z] = steamTable.hV_p(P)
        hfg[z] = hgas[z] - hf[z]
        
        Xe[z] = (enthalpy_actual[z] - hf[z]) / hfg[z]
       
    return (Xe, hfg, hgas)
        