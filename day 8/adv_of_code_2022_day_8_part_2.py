databestand = open('adv_of code_2022_day_8_data.txt','r')
raster = databestand.read().splitlines()
highest_scenic_score = int()
for rij in range(0,len(raster)):
    for boom in range(0,len(raster[rij])):
        factorLinks,factorRechts,factorBoven,factorOnder = 0,0,0,0
        bomenLinks = raster[rij][:boom]
        for boomLinks in range(len(bomenLinks)-1,-1,-1):
            if int(raster[rij][boom])>int(bomenLinks[boomLinks]):
                factorLinks+=1
            else:
                factorLinks+=1
                break
        bomenRechts = raster[rij][boom+1:]
        for boomRechts in range(0,len(bomenRechts)):
            if int(raster[rij][boom])>int(bomenRechts[boomRechts]):
                factorRechts+=1
            else:
                factorRechts+=1
                break
        bomenBoven = []
        for bovenrij in range(0,rij):
            bomenBoven.append(raster[bovenrij][boom])
        for boomBoven in range(len(bomenBoven)-1,-1,-1):
            if int(raster[rij][boom])>int(bomenBoven[boomBoven]):
                factorBoven+=1
            else:
                factorBoven+=1
                break
        bomenOnder = []
        for onderrij in range(rij + 1, len(raster)):
            bomenOnder.append(raster[onderrij][boom])
        for boomOnder in range(0,len(bomenOnder)):
            if int(raster[rij][boom])>int(bomenOnder[boomOnder]):
                factorOnder+=1
            else:
                factorOnder+=1
                break
        scenic_score = factorLinks*factorRechts*factorBoven*factorOnder
        if scenic_score>highest_scenic_score:
            highest_scenic_score=scenic_score
print(f'Hoogste scenic_score: {highest_scenic_score}')
