databestand = open('adv_of_code_2022_day_1_data.txt', 'r')
items = databestand.read().splitlines()
totaalPer = int()
nieuweLijst=[]
for item in items:
    try:
        totaalPer+=int(item)
    except:
        nieuweLijst.append(totaalPer)
        totaalPer=0
nieuweLijst.sort()
print(nieuweLijst[-1])


