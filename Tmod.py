import numpy as n
from scipy.integrate import quad
from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
def Tmod(T_inlet,Linear_Heat_Rate,Actual_Multiplication_Factor,Length_e,Len,massfr,Pitch,FROD,Pressure):
    FRACe = Length_e/100
    FRAC = Len/100
    TMOD = n.zeros(100)
    TMOD[0] = T_inlet 
    Specific_Heat = n.zeros(100)
    Tadd = n.zeros(100)
    A = n.zeros(100)
    integral2 = n.zeros(100)
    now = n.zeros(100)
    enthalpy_actual = n.zeros(100)
    enthalpy_liquid = n.zeros(100)
    Specific_Heat[0] = steamTable.Cp_pt(Pressure,T_inlet)
    enthalpy_liquid[0] = steamTable.hL_t(T_inlet)
    enthalpy_actual[0] = steamTable.h_pt(Pressure, T_inlet ) 
    #integral = n.linspace(0,2,25)
    for c in range(1,100): #coolant
        p = c-50
        integral2[c] = (1 + n.sin((n.pi/Length_e)*(p)*FRACe))
        def eq(p):
            return n.cos((n.pi/Length_e)*(FRAC)*(p))
        A[c],err = quad(eq,-Len/2,p*FRAC)
        #print(A[c])
        #print(integral2[c])
   
        First = (Linear_Heat_Rate/(massfr*Specific_Heat[c-1]))
        Second = (Length_e/n.pi)
        Tadd[c] = First*(integral2[c])*Second
        TMOD[c] = (T_inlet+(Tadd[c]))
        #print(TMOD[z])
        enthalpy_liquid[c] = steamTable.hL_t(TMOD[c])
        enthalpy_actual[c] = steamTable.h_pt(Pressure, TMOD[c])  
        Specific_Heat[c] = steamTable.Cp_pt(Pressure,TMOD[c])
    return(TMOD,enthalpy_liquid,enthalpy_actual,Specific_Heat,integral2,now,A)  
      

