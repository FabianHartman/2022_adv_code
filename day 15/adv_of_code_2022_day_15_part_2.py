import intervaltree
databestand = open('adv_of_code_2022_day_15_data.txt','r')
dataRegels = databestand.read().splitlines()
locatie_sensoren = []
afstanden = []

for dataRegel in range(0,len(dataRegels)):
    dataRegels[dataRegel]=dataRegels[dataRegel].split(':')
for dataRegel in dataRegels:
    sensor_x = int(dataRegel[0][12:dataRegel[0].index(',')])
    sensor_y = int(dataRegel[0][dataRegel[0].index('y=')+2:])
    locatie_sensoren.append([sensor_x,sensor_y])
    baken_x=int(dataRegel[1][24:dataRegel[1].index(',')])
    baken_y=int(dataRegel[1][dataRegel[1].index('y=')+2:])
    afstand = abs(baken_y-sensor_y)+abs(baken_x-sensor_x)
    afstanden.append(afstand)

mogelijke_rijen = []
for rij in range(4000000+1):
    geblokkeerd = []
    for sensor in range(0,len(locatie_sensoren)):

        if abs(locatie_sensoren[sensor][1]-rij)<=afstanden[sensor]:
            verticale_afstand_mogelijk = afstanden[sensor] - abs(locatie_sensoren[sensor][1]-rij)
            geblokkeerd.append([locatie_sensoren[sensor][0]-verticale_afstand_mogelijk,locatie_sensoren[sensor][0]+verticale_afstand_mogelijk])
    try:
        totaalGeblokkeerd = intervaltree.IntervalTree.from_tuples(geblokkeerd)
        totaalGeblokkeerd.merge_overlaps(strict=False)
        if len(totaalGeblokkeerd)>1:
            mogelijke_rijen.append(rij)
    except:
        mogelijke_rijen.append(rij)

for rij in mogelijke_rijen:
    for x in range(0,4000000+1,1):
        buiten_bereik = True
        for sensor in range(0, len(locatie_sensoren)):
            if abs(locatie_sensoren[sensor][1]-rij)+abs(locatie_sensoren[sensor][0]-x)<=afstanden[sensor]:
                buiten_bereik = False
        if buiten_bereik:
            print(x,rij)
            print(x*4000000+rij)



