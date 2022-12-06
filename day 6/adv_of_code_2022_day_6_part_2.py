databestand = open('adv_of_code_2022_day_6_data.txt','r')
puzzle_input = databestand.read()
for char in range(0,len(puzzle_input)-13):
    laatste_veertien = set(puzzle_input[char:char+14])
    if len(laatste_veertien)==14:
        print(char+14)