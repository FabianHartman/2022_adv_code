databestand = open('adv_of_code_2022_day_12_data.txt','r')
grid = databestand.read().splitlines()
mogelijkheden = [(0,1),(0,-1),(1,0),(-1,0)]
for rij in range(0,len(grid)):
    try:
        beginpunt = [grid[rij].index('S'),rij]
        beginpunt_rij = grid[rij]
        nieuwe_beginpunt_rij = ''
        for char in beginpunt_rij:
            if char == 'S':
                nieuwe_beginpunt_rij+='a'
            else:
                nieuwe_beginpunt_rij+=char
        grid[rij]=nieuwe_beginpunt_rij
    except:
        pass
    try:
        eindpunt = [grid[rij].index('E'),rij]
        eindpunt_rij = grid[rij]
        nieuwe_eindpunt_rij = ''
        for char in eindpunt_rij:
            if char == 'E':
                nieuwe_eindpunt_rij += 'z'
            else:
                nieuwe_eindpunt_rij+=char
        grid[rij]=nieuwe_eindpunt_rij
    except:
        pass

def zoek(eindpunt,grid,mogelijkheden):
    wachtrij = []
    toe_te_voegen_aan_wachtrij = [eindpunt]
    E_not_found = True
    bezocht = []
    cycle=0
    while E_not_found:
        cycle+=1
        wachtrij = toe_te_voegen_aan_wachtrij.copy()
        for element in wachtrij:
            for mogelijkheid in mogelijkheden:
                mogelijke_positie = [element[0]+mogelijkheid[0],element[1]+mogelijkheid[1]]
                if 0<=mogelijke_positie[0]<len(grid[0]) and 0<=mogelijke_positie[1]<len(grid):
                    if not mogelijke_positie in wachtrij and not mogelijke_positie in toe_te_voegen_aan_wachtrij and not mogelijke_positie in bezocht:
                        if ord(grid[element[1]][element[0]])<=ord(grid[mogelijke_positie[1]][mogelijke_positie[0]])+1:
                            toe_te_voegen_aan_wachtrij.append(mogelijke_positie)
                            if ord(grid[mogelijke_positie[1]][mogelijke_positie[0]]) == 97:
                                return cycle
            if not element in bezocht:
                bezocht.append(element)
print(zoek(eindpunt,grid,mogelijkheden))

