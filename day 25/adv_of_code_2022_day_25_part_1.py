import math
databestand = open('adv_of_code_2022_day_25_data.txt','r')
SNAFU_numbers = databestand.read().splitlines()
decimal_numbers = []
for SNAFU_number in SNAFU_numbers:
    SNAFU_number_list = list(SNAFU_number)
    for SNAFU_number_element in range(0,len(SNAFU_number_list)):
        if SNAFU_number_list[SNAFU_number_element] == '=':
            SNAFU_number_list[SNAFU_number_element] = -2
        elif SNAFU_number_list[SNAFU_number_element] == '-':
            SNAFU_number_list[SNAFU_number_element] = -1
        else:
            SNAFU_number_list[SNAFU_number_element] = int(SNAFU_number_list[SNAFU_number_element])
    waarde_SNAFU_number = 0
    for number in range(len(SNAFU_number_list)):
        waarde_SNAFU_number_element = SNAFU_number_list[number]*5**(len(SNAFU_number_list)-number-1)
        waarde_SNAFU_number+=waarde_SNAFU_number_element
    decimal_numbers.append(waarde_SNAFU_number)
totaal_decimaal = sum(decimal_numbers)
macht = math.floor(math.log(totaal_decimaal,5))
SNAFU_cumulative = []
resterend = totaal_decimaal
i = 0
while macht-i>=0:
    SNAFU_cumulative.append(resterend//(5**(macht-i)))
    resterend =resterend%(5**(macht-i))
    i+=1
for getal in range(len(SNAFU_cumulative)-1,-1,-1):
    if SNAFU_cumulative[getal]>2:
        SNAFU_cumulative[getal-1]+=1
        if SNAFU_cumulative[getal]==3:
            SNAFU_cumulative[getal]='='
        if SNAFU_cumulative[getal]==4:
            SNAFU_cumulative[getal]='-'
        if SNAFU_cumulative[getal]==5:
            SNAFU_cumulative[getal]=0
resultaat = str()
for element in SNAFU_cumulative:
    resultaat+=str(element)
print(resultaat)



