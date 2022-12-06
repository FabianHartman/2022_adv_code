#data inlezen

databestand = open('adv_of_code_2022_day_5_data.txt','r')
alleData = databestand.read().splitlines()

#alleen het diagram pakken

breedte = 9
for regel in range(0,len(alleData)):
    if alleData[regel] == '':
        max_begin_hoogte = regel-1

#de data omzetten naar stappels letters

supply_stacks_horizontal = alleData[:max_begin_hoogte]
stapels = []
for kolom in range(0,breedte):
    stapel = []
    for supply_laag in range(len(supply_stacks_horizontal) - 1, -1, -1):
        stapel.append(supply_stacks_horizontal[supply_laag][1+4*kolom])
    stapels.append(stapel)

#lege elementen uit de lijst verwijderen

for stapel in stapels:
    while True:
        try:
            stapel.remove(' ')
        except:
            break

#opdrachten inlezen

opdrachten = alleData[max_begin_hoogte+2:]
for opdracht in opdrachten:
    spatielijst = []
    for char in range(0,len(opdracht)):
        if opdracht[char] == ' ':
            spatielijst.append(char)
    aantal = int(opdracht[spatielijst[0]+1:spatielijst[1]])
    van = int(opdracht[spatielijst[2]+1:spatielijst[3]])-1
    tot = int(opdracht[spatielijst[4]+1:])-1

#opdrachten uitvoeren

    for zoveelste in range(0,aantal):
        stapels[tot].append(stapels[van][-1])
        stapels[van].pop()

#het antwoord ophalen

antwoord = str()
for stapel in stapels:
    antwoord += stapel[-1]
print(antwoord)



