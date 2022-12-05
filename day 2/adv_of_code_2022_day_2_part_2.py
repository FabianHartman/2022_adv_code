databestand = open('adv_of_code_2022_day_2_data.txt','r')
rondes = databestand.read().splitlines()
score = int()
for ronde in rondes:
    print(ronde)
    if ronde[0]=='A':
        if ronde[2]=='X':
            score+=3
        if ronde[2] == 'Y':
            score+=4
        if ronde[2]=='Z':
            score+=8
    if ronde[0]=='B':
        if ronde[2]=='X':
            score+=1
        if ronde[2]=='Y':
            score+=5
        if ronde[2] == 'Z':
            score+=9
    if ronde[0]=='C':
        if ronde[2]=='X':
            score+=2
        if ronde[2] == 'Y':
            score+=6
        if ronde[2] == 'Z':
            score+=7
print(score)