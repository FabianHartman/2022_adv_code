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

SteenOfZandLocaties = steenLijst.copy()

def zand(SteenOfZandLocaties,huidige_positie_zand = [500,0]):
    plekken_onder_zand = []
    for steenOfZand in SteenOfZandLocaties:
        if steenOfZand[0]==huidige_positie_zand[0]:
            if steenOfZand[1]>huidige_positie_zand[1]:
                plekken_onder_zand.append(steenOfZand)
    if len(plekken_onder_zand)>0:
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
            return 1
    else:
        return 0
aantalZand = 0

while True:
    if zand(SteenOfZandLocaties)==1:
        aantalZand+=1
    elif zand(SteenOfZandLocaties)==0:
        break
print(aantalZand)




