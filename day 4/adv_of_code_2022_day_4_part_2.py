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
    bereik1 = set()
    bereik2 = set()
    for i in range(start1,eind1+1):
        bereik1.add(i)
    for i in range(start2,eind2+1):
        bereik2.add(i)
    if len(bereik1.intersection(bereik2))>0:
        aantal+=1
print(aantal)