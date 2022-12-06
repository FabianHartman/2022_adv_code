databestand = open('adv_of_code_2022_day_6_data.txt','r')
puzzle_input = databestand.read()
for char in range(0,len(puzzle_input)-3):
    if puzzle_input[char]!=puzzle_input[char+1] and puzzle_input[char]!=puzzle_input[char+2] and puzzle_input[char]!=puzzle_input[char+3]:
        if puzzle_input[char+1]!=puzzle_input[char+2] and puzzle_input[char+1]!=puzzle_input[char+3]:
            if puzzle_input[char+2]!=puzzle_input[char+3]:
                print(char+4)
                break