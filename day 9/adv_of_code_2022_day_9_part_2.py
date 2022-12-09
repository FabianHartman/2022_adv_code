from time import perf_counter_ns as pfc
begin = pfc()
databestand = open('adv_of_code_2022_day_9_data.txt','r')
stappen = databestand.read().splitlines()
positiesGeweestTail = list()
huidigeLocatieHead = [0,0]
huidigeLocatieTails = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for stap in stappen:
    stap = stap.split(' ')
    for tussenstap in range(0,int(stap[1])):                                                                            #per tussenstap
        if stap[0]=='U':                                                                                                #omhoog
            huidigeLocatieHead[1]+=1
        if stap[0]=='D':                                                                                                #omlaag
            huidigeLocatieHead[1]-=1
        if stap[0]=='L':                                                                                                #naar links
            huidigeLocatieHead[0]-=1
        if stap[0]=='R':                                                                                                #naar rechts
            huidigeLocatieHead[0]+=1
        for taildeel in range(0,len(huidigeLocatieTails)):                                                              #per deel van de tail
            if taildeel==0:
                if abs(huidigeLocatieHead[0]-huidigeLocatieTails[0][0])>1 or abs(huidigeLocatieHead[1]-huidigeLocatieTails[0][1])>1:    #als de tail moet verplaatsen
                    if huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==2:                                                          #verschuiving naar de bovenste drie mogelijkheden
                        if huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                            huidigeLocatieTails[0][0] += 1
                            huidigeLocatieTails[0][1] += 1
                        elif huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==-1:                                                   #als de tail naar linksboven moet verplaatsen
                            huidigeLocatieTails[0][0] -=1
                            huidigeLocatieTails[0][1] +=1
                        else:                                                                                                   #als de tail enkel naar boven moet verplaatsen
                            huidigeLocatieTails[0][1] +=1
                    if huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==-2:                                                         #verschuiving naar de linker drie mogelijkheden
                        if huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==1:                                                      #als de tail naar linksboven moet verplaatsen
                            huidigeLocatieTails[0][0]-=1
                            huidigeLocatieTails[0][1]+=1
                        elif huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                            huidigeLocatieTails[0][0]-=1
                            huidigeLocatieTails[0][1]-=1
                        else:                                                                                                   #als de tail enkel naar links moet verplaatsen
                            huidigeLocatieTails[0][0]-=1
                    if huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==2:                                                          #verschuiving naar de rechter drie mogelijkheden
                        if huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                            huidigeLocatieTails[0][0]+=1
                            huidigeLocatieTails[0][1]+=1
                        elif huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==-1:                                                   #als de tail naar rechtsonder moet verplaatsen
                            huidigeLocatieTails[0][0]+=1
                            huidigeLocatieTails[0][1]-=1
                        else:                                                                                                   #als de tail enkel naar rechts moet verplaatsen
                            huidigeLocatieTails[0][0]+=1
                    if huidigeLocatieHead[1]-huidigeLocatieTails[0][1]==-2:                                                         #verschuiving naar de onderste drie mogelijkheden
                        if huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==1:                                                      #als de tail naar rechtsonder moet verplaatsen
                            huidigeLocatieTails[0][0]+=1
                            huidigeLocatieTails[0][1]-=1
                        elif huidigeLocatieHead[0]-huidigeLocatieTails[0][0]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                            huidigeLocatieTails[0][0]-=1
                            huidigeLocatieTails[0][1]-=1
                        else:                                                                                                   #als de tail enkel naar onder moet verplaatsen
                            huidigeLocatieTails[0][1]-=1

            else:                                                                                                       #niet het eerste staartdeel
                if abs(huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]) > 1 or abs(huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1]) > 1:  # als de tail moet verplaatsen
                    if abs(huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]) > 1 and abs(huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1]) > 1: #als de tail wortel(8) van de voorganger is verwijderd
                        if huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]==2 and huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1] == 2:     #rechtsboven
                            huidigeLocatieTails[taildeel][0]+=1
                            huidigeLocatieTails[taildeel][1]+=1
                        if huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]==-2 and huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1] == 2:    #linksboven
                            huidigeLocatieTails[taildeel][0]-=1
                            huidigeLocatieTails[taildeel][1]+=1
                        if huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]==2 and huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1] == -2:    #rechtsonder
                            huidigeLocatieTails[taildeel][0]+=1
                            huidigeLocatieTails[taildeel][1]-=1
                        if huidigeLocatieTails[taildeel-1][0] - huidigeLocatieTails[taildeel][0]==-2 and huidigeLocatieTails[taildeel-1][1] - huidigeLocatieTails[taildeel][1] == -2:   #linksonder
                            huidigeLocatieTails[taildeel][0]-=1
                            huidigeLocatieTails[taildeel][1]-=1
                    else:
                        if huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==2:                                                          #verschuiving naar de bovenste drie mogelijkheden
                            if huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                                huidigeLocatieTails[taildeel][0] += 1
                                huidigeLocatieTails[taildeel][1] += 1
                            elif huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==-1:                                                   #als de tail naar linksboven moet verplaatsen
                                huidigeLocatieTails[taildeel][0] -=1
                                huidigeLocatieTails[taildeel][1] +=1
                            else:                                                                                                   #als de tail enkel naar boven moet verplaatsen
                                huidigeLocatieTails[taildeel][1] +=1
                        if huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==2:                                                          #verschuiving naar de rechter drie mogelijkheden
                            if huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                                huidigeLocatieTails[taildeel][0]+=1
                                huidigeLocatieTails[taildeel][1]+=1
                            elif huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==-1:                                                   #als de tail naar rechtsonder moet verplaatsen
                                huidigeLocatieTails[taildeel][0]+=1
                                huidigeLocatieTails[taildeel][1]-=1
                            else:                                                                                                   #als de tail enkel naar rechts moet verplaatsen
                                huidigeLocatieTails[taildeel][0]+=1
                        if huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==-2:                                                         #verschuiving naar de linker drie mogelijkheden
                            if huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==1:                                                      #als de tail naar linksboven moet verplaatsen
                                huidigeLocatieTails[taildeel][0]-=1
                                huidigeLocatieTails[taildeel][1]+=1
                            elif huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                                huidigeLocatieTails[taildeel][0]-=1
                                huidigeLocatieTails[taildeel][1]-=1
                            else:                                                                                                   #als de tail enkel naar links moet verplaatsen
                                huidigeLocatieTails[taildeel][0]-=1

                        if huidigeLocatieTails[taildeel-1][1]-huidigeLocatieTails[taildeel][1]==-2:                                                         #verschuiving naar de onderste drie mogelijkheden
                            if huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==1:                                                      #als de tail naar rechtsonder moet verplaatsen
                                huidigeLocatieTails[taildeel][0]+=1
                                huidigeLocatieTails[taildeel][1]-=1
                            elif huidigeLocatieTails[taildeel-1][0]-huidigeLocatieTails[taildeel][0]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                                huidigeLocatieTails[taildeel][0]-=1
                                huidigeLocatieTails[taildeel][1]-=1
                            else:                                                                                                   #als de tail enkel naar onder moet verplaatsen
                                huidigeLocatieTails[taildeel][1]-=1
        if huidigeLocatieTails[8] not in positiesGeweestTail:                                                               #als deze locatie van de tail nog niet in de lijst staat
            positiesGeweestTail.append([huidigeLocatieTails[8][0],huidigeLocatieTails[8][1]])
print(str(len(positiesGeweestTail)) + ' posities')
eind = pfc()
print(str((eind-begin)/1000000000) + ' seconden')
