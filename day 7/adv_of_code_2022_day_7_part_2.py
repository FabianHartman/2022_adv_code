breadcrumbs = ''
mappen = dict()
databestand = open('adv_of_code_2022_day_7_data.txt','r')
regels_databestand = databestand.read().splitlines()
totaal = int()
for regel in regels_databestand:
    if regel[:4] == '$ cd':
        if regel[5:]== '..':
            breadcrumbs = breadcrumbs[:breadcrumbs[:breadcrumbs.rfind('/')].rfind('/')+1]
        else:
            breadcrumbs += regel[5:]+'/'
            mappen[breadcrumbs]=0
    if regel[0] in '1234567890':
        mappen[breadcrumbs] += int(regel[:regel.index(' ')])
for plek in mappen.keys():
    huidige_plek = plek
    while len(huidige_plek) > 2:
        map_boven_map = huidige_plek[:huidige_plek[:huidige_plek.rfind('/')].rfind('/')+1]
        mappen[map_boven_map]+=mappen[plek]
        huidige_plek = map_boven_map

opslag_nog_nodig = 30000000-(70000000-mappen['//'])

minst_groot_boven_benodigd = 9999999999999999999999999999
for map in mappen:
    if mappen[map]<minst_groot_boven_benodigd and mappen[map]>=opslag_nog_nodig:
        minst_groot_boven_benodigd=mappen[map]

print(minst_groot_boven_benodigd)