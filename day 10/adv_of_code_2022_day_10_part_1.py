databestand = open('adv_of_code_2022_day_10_data.txt', 'r')
regels = databestand.read().splitlines()
cycle = 0
X = 1
totaal = 0
def get_signal_strength(cycle,X):
    return cycle*X

for regel in regels:
    if regel[:4] == 'noop':
        cycle+=1
        if (cycle-20)%40==0 and cycle<240:
            totaal+=(get_signal_strength(cycle,X))
    if regel[:4] == 'addx':
        cycle+=1
        if (cycle-20)%40==0 and cycle<240:
            totaal+=(get_signal_strength(cycle,X))
        cycle+=1
        if (cycle-20)%40==0 and cycle<240:
            totaal+=(get_signal_strength(cycle,X))
        X+=int(regel[5:])
print(f'Totaal={totaal}')