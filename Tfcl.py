import scipy
import math as m
import numpy as n
from pyXSteam.XSteam import XSteam #Table of possible water properties
steamTable = XSteam(XSteam.UNIT_SYSTEM_BARE)
def Tfcl(Burnup,T_inlet,Q0prime,Actual_Multiplication_Factor,integral999,massfr,Specific_Heat,Le,FRAC,Rco,Rci,Roo,Rg,hg,h,ko,kc,do,FRACr,Rf,dRf):
    Tfcl = n.zeros(((100,100,len(Burnup))))
    J0 = n.zeros(100)
    Tmax = n.zeros(len(Burnup))
    zmax = n.zeros((len(Burnup)))
    know = n.zeros(((100,100,len(Burnup))))
    RTHO2 = 0.001586277
    Sixth = n.zeros(((100,100,len(Burnup))))
    FRACr = Rf/100
    
    for i in range(0,20):
            know[0,0,i] = kTHO2(int(700),Burnup[i]) / 1000
            
            for r in range(0,100):
                J0[r] = scipy.special.j0((2.405 * r * FRACr)/(Rf+dRf))
            for z in range(0,100):
                for r in range(0,100):
                    First =(Le/(m.pi*massfr*Specific_Heat[z]))*(((integral999[z])))
                    Second = ((1/(2*m.pi*Roo*h)))
                    Third = (do/(2*m.pi*Roo*ko))
                    Fourth = ((1/(2*m.pi*kc))*n.log(Rco/Rci))
                    Fifth = (1/(2*m.pi*Rg*hg))
                    Sixth = (1/(4*m.pi*know[r,z,i]))
                    Seventh = Actual_Multiplication_Factor[(z+1)*4]
                    Tfcl[r,z,i] = (T_inlet + J0[r]*Q0prime*(First+(Second+Third+Fourth+Fifth+Sixth)*Seventh))
                    if r <= 98:
                        if r*FRACr > RTHO2:
                            know[r+1,z,i] =  kUO2(Tfcl[r,z,i],Burnup[i]) / 1000
                        else:
                            know[r+1,z,i] =  kTHO2(Tfcl[r,z,i],Burnup[i]) / 1000
                    if r == 99 and i == 0:
                            if z <= 98:
                                '''f r*FRACr > RTHO2:
                                know[0,z+1,i] = kUO2(Tfcl[0,z,i],Burnup[i]) / 1000
                                elif r*FRACr < RTHO2:'''
                                know[0,z+1,i] =kTHO2(Tfcl[0,z,i],Burnup[i]) / 1000
                                
                    if r == 99 and i > 0:
                           if z <= 98:
                               '''if r*FRACr >= RTHO2:
                                   know[0,z+1,i] = kUO2(Tfcl[0,z+1,i-1],Burnup[i]) / 1000
                               elif r*FRACr < RTHO2:'''
                               know[0,z+1,i] = kTHO2(Tfcl[0,z,i],Burnup[i]) / 1000
                               
            
        
                    
                        
    
    
    
    
    
    
    for x in range(len(Burnup)):    
        Tmax[x] = n.nanmax(Tfcl[0,:,x]) 
        zmax[x] = n.argmax(Tfcl[0,:,x])
    
    BurnupStep = n.argmax(Tmax[:])   
     
    TFCLarray = n.zeros(((100,100,len(Burnup))))
    TFCLarray[:,:,:] = Tfcl[:,:,:]
    return (TFCLarray, Tmax, zmax, BurnupStep, know,J0 , Sixth)


    

