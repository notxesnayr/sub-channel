import numpy as n
def look():
    #fobj = open('mctal_1.txt','r')
    fobj = open('mctal2.txt','r')#Creating the AXIAL POWER DISTRIBUTION WORKS
    lines = []
    words = []
    with fobj as f: #Splitting file into words and looking for input files as well as answers
        for line in f:
            lines.append(line)
            for word in line.split():
                words.append(word)
    A = len(words)
    APD = []
    for z in range(0,A):
        if words[z] == r'd':
            if words[z+1] == r'1':
                if words[z+2] == r'u':
                    if words[z+3] == r'1':
                        for i in range(15,816):
                            if (i%2) ==1:
                                APD.append(words[z+i])
                    
    lines2=[]
    words2=[]
    #fobj2 = open('Th_cycle1_output.txt','r')
    fobj2 = open('Th_cycle2_one.txt','r')
    #fobj2 = open('Uranium.txt','r')
    fobj3 = open('Th_cycle2_two.txt','r')
    '''fobj2 = open('Th1.1.txt','r')#Opening the files
    fobj3 = open('Th1.2.txt','r')
    fobj4 = open('Th1.3.txt','r')
    fobj5 = open('Th1.4.txt','r')
    fobj6 = open('Th1.5.txt','r')'''
    with fobj2 as f2:#Opening each file and adding it to one word list and one line list
        for line in f2:
            lines2.append(line)
            for word in line.split():
                    words2.append(word)
    with fobj3 as f3:
        for line in f3:
            lines2.append(line)
            for word in line.split():
                words2.append(word)
    '''with fobj4 as f4:
        for line in f4:
            lines.append(line)
            for word in line.split():
                words2.append(word)
    with fobj5 as f5:
        for line in f5:
            lines2.append(line)
            for word in line.split():
                words2.append(word)
    with fobj6 as f6:
        for line in f6:
            lines2.append(line)
            for word in line.split():
                words2.append(word)'''
    B = len(lines2)#Finding amount of lines and words total
    #print(B)
    RRD1=[]
    for z in range(0,B):#Setting the date ranges
        if lines2[z].startswith(r'* Correcter calc'):
            (Garbage,RD) = lines2[z].split('=')
            (RRD,Garbage2) = RD.split(' ')
            if RRD not in RRD1:
                RRD1.append(RRD)
    Tally34lol = []  
    Tally44lol = []
    Tally24lol = []
    Tally14lol = []
    
    FDR = n.zeros(len(RRD1)+1)
    
    for z in range(0,len(FDR),2):
        [FD,SD] = RRD1[z].split(',')
        Garbage, FDR[z] = FD.split('[')
        FDR[z+1],Garbage = SD.split(']')        
    
    for z in range(0,B):#Setting the code to imput the cell name and ?Power? 
            for g in [37,27,47,57]:
                if lines2[z].startswith(r'1tally' + '       ' + str(g)) == True:

                        if g == 37:
                            for y in range(0,147,3):
                                if lines2[z+y+9].startswith(r' cell') == True:
                                    #if lines2[z+y+10] not in Tally14lol:#Making sure the fact that multiple codes where opened not repeat
                                            Tally14lol.append(lines2[z+9+y])
                                            Tally14lol.append(lines2[z+10+y])
                        
                        
                        #14
                        if g == 27:
                            for yy in range(0,12,3):
                                if lines2[z+yy+9].startswith(r' cell') == True:
                                    #if lines2[z+yy+10] not in Tally24lol:
                                        Tally24lol.append(lines2[z+9+yy])
                                        Tally24lol.append(lines2[z+10+yy])
                               
                        if g == 47:
                            for y in range(0,144,3):
                                if lines2[z+y+10].startswith(r' cell') == True:
                                    #if lines2[z+y+11] not in Tally34lol:
                                        Tally34lol.append(lines2[z+10+y])
                                        Tally34lol.append(lines2[z+11+y])
                              
                        if g == 57:
                            for y in range(0,168,3):
                                if lines2[z+y+10].startswith(r' cell') == True:
                                    #if lines2[z+y+11] not in Tally44lol[:]:
                                        Tally44lol.append(lines2[z+10+y])
                                        Tally44lol.append(lines2[z+11+y])
  
   
        
    
    #Numbers = n.sort(Keep[:])
    #for x in range(160):
        #if x%2 != 0:
            #V[x] = 
    Burnupn = []
    Burnup = n.zeros(len(FDR))
    
    for z in range(0,B):
        if lines2[z].startswith(r' step  duration     time       power     keff      flux    ave. nu    ave. q    b') == True:
            i = 0
            for c in range(len(FDR)):
                Burnupn.append(lines2[z+2+i])
                i += 1
   
    for v in range(len(FDR)):
        a,b,c,d,e,f,g,h,i,j = Burnupn[v].split()
        Burnup[v] = i
    #for v in range(len(FDR)):
        #A,B,C,D,E,F = Burnup[v].split()
        #print(A,B,C,D,E,F,G,H,I)
    for x in [39,37,35,33,31,29,27,25,23,21,19,17,15,13,11,9,7,5,3,1]:         
        kkk = (x*98) + 98
        jjj = (x*8) + 8
        lll = (x*96) + 96
        ppp = (x*112) + 112
        del Tally14lol[(x*98):kkk]
        del Tally24lol[(x*8):jjj]
        del Tally34lol[(x*96):lll]
        del Tally44lol[(x*112):ppp]
    print(len(Tally14lol)/98)#Number of Times each one ran SHOULD BE EQUAL
    print(len(Tally24lol)/8)                                    
    print(len(Tally34lol)/96)                     
    print(len(Tally44lol)/112)
    
    H = n.zeros(int(len(Tally14lol)/2))
    HH = n.zeros(int(len(Tally24lol)/2))
    HHH = n.zeros(int(len(Tally34lol)/2))
    HHHH = n.zeros(int(len(Tally44lol)/2))
    for x in range(1,int(len(Tally14lol)),2):
        G = Tally14lol[x].strip()
        [H[int((x-1)/2)],Garbage] = G.split()
    for y in range(1,int(len(Tally24lol)),2):
        G = Tally24lol[y].strip()
        [HH[int((y-1)/2)],Garbage] = G.split()
    for y in range(1,len(Tally34lol),2):
        G = Tally34lol[y].strip()
        [HHH[int((y-1)/2)],Garbage] = G.split()
    for y in range(1,len(Tally44lol),2):
        G = Tally44lol[y].strip()
        [HHHH[int((y-1)/2)],Garbage] = G.split()
    Cells14 = []
    Cells24 = []
    Cells34 = []
    Cells44 = []
    for x in range(0,98,2):
        Cells14.append(Tally14lol[x])
    for y in range(0,8,2):
        Cells24.append(Tally24lol[y])
    for z in range(0,96,2):
        Cells34.append(Tally34lol[z])
    for z in range(0,112,2):    
        Cells44.append(Tally44lol[z])
    u = 0
    uu = 0
    uuu = 0
    uuuu = 0
    Y = n.zeros((49,len(FDR)))
    YY = n.zeros((4,len(FDR)))
    YYY = n.zeros((48,len(FDR)))
    YYYY = n.zeros((56,len(FDR)))
    for y in range(len(FDR)):
        for x in range(49):
            Y[x,y] = H[u]
            u+=1
        for z in range(4):
            YY[z,y] = HH[uu]
            uu+=1
        for v in range(48):
            YYY[v,y] = HHH[uuu]
            uuu+=1
        for f in range(56):
            YYYY[f,y] = HHHH[uuuu]
            uuuu += 1
    
    
    
    '''NUMBERS1 = n.sum(Y,axis=1)
    NUMBERS2 = n.sum(YY,axis=1)
    NUMBERS3 = n.sum(YYY,axis=1)
    NUMBERS4 = n.sum(YYYY,axis=1)
    
    Numbers1 = n.argsort(NUMBERS1)
    Numbers2 = n.argsort(NUMBERS2)
    Numbers3 = n.argsort(NUMBERS3)
    Numbers4 = n.argsort(NUMBERS4)'''    
    mAPD = n.zeros(401)       
   
    APDAF = 0               


                


    for q in range(len(APD)):
        APDAF += float(APD[q])
        mAPD[q] = float(APD[q])
    AverageAPD = APDAF / (401) 
    maxAPD = n.nanmax(mAPD[:])
    PFAPD = maxAPD/AverageAPD
    MultiplicationFactor1 = 1/n.nanmax(mAPD[:])
    Actual_Multiplication_Factor = n.zeros(401)
    for q in range(401):
        Actual_Multiplication_Factor[q] = float(APD[q]) * MultiplicationFactor1
    print('The Axial Peaking Factor is', PFAPD)

    
    return Cells14,Cells24,Cells34,Cells44,Tally34lol,Tally44lol,Tally24lol,Tally14lol,APD,RRD1,FDR,Y,YY,YYY,YYYY,Actual_Multiplication_Factor,Burnup,PFAPD
Cells14,Cells24,Cells34,Cells44,Tally34lol,Tally44lol,Tally24lol,Tally14lol,APD,RRD1,FDR,Y,YY,YYY,YYYY,Actual_Multiplication_Factor,Burnup,PFAPD = look()



           
    
    




             
