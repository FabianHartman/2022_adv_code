databestand = open('adv_of_code_2022_day_14_data.txt','r')
data = databestand.read().splitlines()
for regel in range(0,len(data)):
    regelOnderdelen = data[regel].replace(',','.').split(' -> ')
    regelOnderdelenLijst = []
    for regelOnderdeel in regelOnderdelen:
        regelOnderdelenLijst.append(regelOnderdeel)
    data[regel]=regelOnderdelenLijst


steenLijst = []

for path in range(0,len(data),1):
    for hoek in range(0,len(data[path])-1,1):
        huidigeHoek = data[path][hoek].split('.')
        volgendeHoek = data[path][hoek+1].split('.')
        if huidigeHoek[0]==volgendeHoek[0]:
            if int(huidigeHoek[1])>int(volgendeHoek[1]):
                for i in range(int(volgendeHoek[1]),int(huidigeHoek[1])+1):
                    if not [int(huidigeHoek[0]),i] in steenLijst:
                        steenLijst.append([int(huidigeHoek[0]),i])
            if int(huidigeHoek[1])<int(volgendeHoek[1]):
                for i in range(int(huidigeHoek[1]),int(volgendeHoek[1])+1):
                    if not [int(huidigeHoek[0]),i] in steenLijst:
                        steenLijst.append([int(huidigeHoek[0]),i])
        if huidigeHoek[1]==volgendeHoek[1]:
            if int(huidigeHoek[0])>int(volgendeHoek[0]):
                for i in range(int(volgendeHoek[0]),int(huidigeHoek[0])+1):
                    if not [i,int(huidigeHoek[1])] in steenLijst:
                        steenLijst.append([i,int(huidigeHoek[1])])
            if int(huidigeHoek[0])<int(volgendeHoek[0]):
                for i in range(int(huidigeHoek[0]),int(volgendeHoek[0])+1):
                    if not [i,int(huidigeHoek[1])] in steenLijst:
                        steenLijst.append([i,int(huidigeHoek[1])])
hoogste = 0
linkste = int(9e9)
rechtste = 0
for steen in steenLijst:
    if steen[1]>hoogste:
        hoogste = steen[1]
    if steen[0]<linkste:
        linkste = steen[0]
    if steen[0]>rechtste:
        rechtste = steen[0]
for locatie in range(linkste-2000,rechtste+2000,1):
    steenLijst.append([locatie,hoogste+2])

SteenOfZandLocaties = steenLijst.copy()

def zand(SteenOfZandLocaties,huidige_positie_zand = [500,0]):
    while not [huidige_positie_zand[0],huidige_positie_zand[1]+1] in SteenOfZandLocaties:
        huidige_positie_zand = [huidige_positie_zand[0],huidige_positie_zand[1]+1]
    if not [huidige_positie_zand[0]-1,huidige_positie_zand[1]+1] in SteenOfZandLocaties:
        huidige_positie_zand = [huidige_positie_zand[0]-1,huidige_positie_zand[1]+1]
        return zand(SteenOfZandLocaties,huidige_positie_zand)
    elif not [huidige_positie_zand[0]+1,huidige_positie_zand[1]+1] in SteenOfZandLocaties:
        huidige_positie_zand = [huidige_positie_zand[0]+1,huidige_positie_zand[1]+1]
        return zand(SteenOfZandLocaties,huidige_positie_zand)
    else:
        SteenOfZandLocaties.append(huidige_positie_zand)
        if huidige_positie_zand == [500,0]:
            return 0
        return 1
aantalZand = 0

while True:
    if zand(SteenOfZandLocaties)==1:
        aantalZand+=1
    elif zand(SteenOfZandLocaties)==0:
        aantalZand+=1
        break
print(aantalZand)




