import math as m
import numpy as n

from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)

def Tco(Ti,Q0prime,Actual_Multiplication_Factor,integral,massfr,Le,Len,Rco,Cp,FROD,De):
    Tco = n.zeros(100)
    FRAC = Len/100
    hl = n.zeros(100)
    HeatFlux = n.zeros(100)
    Q = n.zeros(100)
    Tci = n.zeros(100)
    h = 34
    CT = 0.572 / 1000
    kc = 0.01385
    hl[0] = steamTable.hL_t(Ti)
    Tco[0] = Ti + ((Q0prime/(2*m.pi*Rco*h )) * Actual_Multiplication_Factor[0])
   
    for y in range(1,100):
        First = (Le/(m.pi*massfr*Cp[y-1]))*(integral[y])
        Second = (1/(2*m.pi*Rco*h))*(Actual_Multiplication_Factor[y*4])
        Tco[y] = (Ti + Q0prime*(First+Second))
    for v in range(0,100):
        Ph = m.pi*2*Rco
        Q[v] = Q0prime * Actual_Multiplication_Factor[v*4]
        HeatFlux[v] = (Q[v]/ Ph)
        Tci[v] = Tco[v] + ((HeatFlux[v] * CT)/kc)
    
        
        
    TCO = n.zeros(100)
    TCI = n.zeros(100)    
    zmax1 = n.argmax(Tco)
    ZMAX1 = zmax1 * FRAC
    TMCO = Tco[zmax1]
    zmax3 = n.argmax(Tci)
    ZMAX3 = zmax3*FRAC
    TMCI = Tci[zmax3]
    TCO[:] = Tco[:]
    TCI[:] = Tci[:]
    return (TCO, ZMAX1, TMCO, zmax1, TCI, ZMAX3, TMCI, HeatFlux)
