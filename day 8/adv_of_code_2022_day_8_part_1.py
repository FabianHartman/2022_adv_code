databestand = open('adv_of code_2022_day_8_data.txt','r')
raster = databestand.read().splitlines()
aantalZichtbaar = int()

for rij in range(0,len(raster)):
    for boom in range(0,len(raster[rij])):
        zichtbaarLinks,zichtbaarRechts,zichtbaarBoven,zichtbaarOnder = True,True,True,True
        for linkerboom in raster[rij][:boom]:
            if int(linkerboom)>=int(raster[rij][boom]):
                zichtbaarLinks = False
        for rechterboom in raster[rij][boom+1:]:
            if int(rechterboom)>=int(raster[rij][boom]):
                zichtbaarRechts = False
        bomenBoven = []
        for bovenrij in range(0,rij):
            bomenBoven.append(raster[bovenrij][boom])
        for boomBoven in bomenBoven:
            if int(boomBoven)>=int(raster[rij][boom]):
                zichtbaarBoven = False
        bomenOnder = []
        for onderrij in range(rij + 1, len(raster)):
            bomenOnder.append(raster[onderrij][boom])
        for boomOnder in bomenOnder:
            if int(boomOnder)>=int(raster[rij][boom]):
                zichtbaarOnder = False
        if (zichtbaarLinks or zichtbaarRechts or zichtbaarBoven or zichtbaarOnder):
            aantalZichtbaar+=1
print(f'Aantal zichtbare bomen van buitenaf: {aantalZichtbaar}')
