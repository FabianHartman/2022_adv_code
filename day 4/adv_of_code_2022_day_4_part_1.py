databestand = open('adv_of_code_2022_day_4_data.txt','r')
range_pairs = databestand.read().splitlines()
aantal = int()
for range_pair in range_pairs:
    dubbel = False
    komma_locatie = range_pair.index(',')
    range1 = range_pair[:komma_locatie]
    range2= range_pair[komma_locatie+1:]
    start1 = int(range1[:range1.index('-')])
    eind1 = int(range1[range1.index('-')+1:])
    start2 = int(range2[:range2.index('-')])
    eind2 = int(range2[range2.index('-')+1:])
    if start2>=start1 and eind2<=eind1 and dubbel==False:
        aantal+=1
        dubbel = True
    if start1>=start2 and eind1<=eind2 and dubbel == False:
        aantal+=1
        dubbel = True
print(aantal)