databestand = open('adv_of_code_2022_day_9_data.txt','r')
stappen = databestand.read().splitlines()
positiesGeweestTail = list()
huidigeLocatieHead = [0,0]
huidigeLocatieTail = [0,0]
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
        if abs(huidigeLocatieHead[0]-huidigeLocatieTail[0])>1 or abs(huidigeLocatieHead[1]-huidigeLocatieTail[1])>1:    #als de tail moet verplaatsen
            if huidigeLocatieHead[1]-huidigeLocatieTail[1]==2:                                                          #verschuiving naar de bovenste drie mogelijkheden
                if huidigeLocatieHead[0]-huidigeLocatieTail[0]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                    huidigeLocatieTail[0] += 1
                    huidigeLocatieTail[1] += 1
                elif huidigeLocatieHead[0]-huidigeLocatieTail[0]==-1:                                                   #als de tail naar linksboven moet verplaatsen
                    huidigeLocatieTail[0] -=1
                    huidigeLocatieTail[1] +=1
                else:                                                                                                   #als de tail enkel naar boven moet verplaatsen
                    huidigeLocatieTail[1] +=1
            if huidigeLocatieHead[0]-huidigeLocatieTail[0]==-2:                                                         #verschuiving naar de linker drie mogelijkheden
                if huidigeLocatieHead[1]-huidigeLocatieTail[1]==1:                                                      #als de tail naar linksboven moet verplaatsen
                    huidigeLocatieTail[0]-=1
                    huidigeLocatieTail[1]+=1
                elif huidigeLocatieHead[1]-huidigeLocatieTail[1]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                    huidigeLocatieTail[0]-=1
                    huidigeLocatieTail[1]-=1
                else:                                                                                                   #als de tail enkel naar links moet verplaatsen
                    huidigeLocatieTail[0]-=1
            if huidigeLocatieHead[0]-huidigeLocatieTail[0]==2:                                                          #verschuiving naar de rechter drie mogelijkheden
                if huidigeLocatieHead[1]-huidigeLocatieTail[1]==1:                                                      #als de tail naar rechtsboven moet verplaatsen
                    huidigeLocatieTail[0]+=1
                    huidigeLocatieTail[1]+=1
                elif huidigeLocatieHead[1]-huidigeLocatieTail[1]==-1:                                                   #als de tail naar rechtsonder moet verplaatsen
                    huidigeLocatieTail[0]+=1
                    huidigeLocatieTail[1]-=1
                else:                                                                                                   #als de tail enkel naar rechts moet verplaatsen
                    huidigeLocatieTail[0]+=1
            if huidigeLocatieHead[1]-huidigeLocatieTail[1]==-2:                                                         #verschuiving naar de onderste drie mogelijkheden
                if huidigeLocatieHead[0]-huidigeLocatieTail[0]==1:                                                      #als de tail naar rechtsonder moet verplaatsen
                    huidigeLocatieTail[0]+=1
                    huidigeLocatieTail[1]-=1
                elif huidigeLocatieHead[0]-huidigeLocatieTail[0]==-1:                                                   #als de tail naar linksonder moet verplaatsen
                    huidigeLocatieTail[0]-=1
                    huidigeLocatieTail[1]-=1
                else:                                                                                                   #als de tail enkel naar onder moet verplaatsen
                    huidigeLocatieTail[1]-=1
        if huidigeLocatieTail not in positiesGeweestTail:                                                               #als deze locatie van de tail nog niet in de lijst staat
            positiesGeweestTail.append([huidigeLocatieTail[0],huidigeLocatieTail[1]])
print(len(positiesGeweestTail))

