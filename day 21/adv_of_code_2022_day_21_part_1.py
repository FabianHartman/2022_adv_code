with open("adv_of_code_2022_day_21_data.txt","r") as dataFile:
    dataRegels = dataFile.read().splitlines()
listNoOperations,listWithOperations = [],[]
monkey_dict = {}
monkey_values = {}
for dataRegel in dataRegels:
    dataRegel = dataRegel.split(':')
    dataRegel[1] = dataRegel[1].strip()
    monkey_dict[dataRegel[0]]=dataRegel[1]
    try:
        int(dataRegel[1])
        listNoOperations.append(dataRegel[0])

    except:
        listWithOperations.append(dataRegel[0])

for monk in listNoOperations:
    monkey_values[monk] = int(monkey_dict[monk])

def calcValue(monkey_dict,monkey_values, monk):
    first_monkey_dependency = monkey_dict[monk][0:4]
    second_monkey_dependency = monkey_dict[monk][7:11]
    operation_type = monkey_dict[monk][5]
    if first_monkey_dependency not in monkey_values:
        waarde_monkey_1 = calcValue(monkey_dict,monkey_values,first_monkey_dependency)
    else:
        waarde_monkey_1 = monkey_values[first_monkey_dependency]
    if second_monkey_dependency not in monkey_values:
        waarde_monkey_2 = calcValue(monkey_dict,monkey_values,second_monkey_dependency)
    else:
        waarde_monkey_2 = monkey_values[second_monkey_dependency]

    if operation_type == '+':
        return waarde_monkey_1+waarde_monkey_2
    elif operation_type == '/':
        return waarde_monkey_1/waarde_monkey_2
    elif operation_type == '*':
        return waarde_monkey_1*waarde_monkey_2
    elif operation_type == '-':
        return waarde_monkey_1-waarde_monkey_2

    return 0
print(calcValue(monkey_dict,monkey_values,'root'))
