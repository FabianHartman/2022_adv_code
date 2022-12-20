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

rij = 2000000
geblokkeerd = []
geblokkeerde_plekken = set()

for sensor in range(0,len(locatie_sensoren)):
    if abs(locatie_sensoren[sensor][1]-rij)<=afstanden[sensor]:
        verticale_afstand_mogelijk = afstanden[sensor] - abs(locatie_sensoren[sensor][1]-rij)
        geblokkeerd.append([locatie_sensoren[sensor][0]-verticale_afstand_mogelijk,locatie_sensoren[sensor][0]+verticale_afstand_mogelijk])

for blokade in geblokkeerd:
    for i in range(blokade[0],blokade[1]+1,1):
        geblokkeerde_plekken.add(i)
print(len(geblokkeerde_plekken)-1)


