databestand = open('adv_of_code_2022_day_10_data.txt', 'r')
regels = databestand.read().splitlines()
cycle = 0
X = 1
hor = 0
ver = 0
scherm = [[],[],[],[],[],[],[]]
def pixel_op_scherm(scherm,hor,ver,X):
    if hor in [X-1,X,X+1]:
        scherm[ver].append('#')
    else:
        scherm[ver].append('.')

for regel in regels:
    if regel[:4] == 'noop':
        cycle+=1
        if (cycle-1)%40==0:
            ver+=1
        hor = (cycle-1)%40
        pixel_op_scherm(scherm,hor,ver,X)
    if regel[:4] == 'addx':
        cycle+=1
        if (cycle-1)%40==0:
            ver+=1
        hor = (cycle-1)%40
        pixel_op_scherm(scherm,hor,ver,X)
        cycle+=1
        if (cycle-1)%40==0:
            ver+=1
        hor = (cycle-1)%40
        pixel_op_scherm(scherm,hor,ver,X)
        X+=int(regel[5:])
for rij in scherm:
    print(''.join(rij))