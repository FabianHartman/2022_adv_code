from math import lcm
databestand = open('adv_of_code_2022_day_11_data.txt','r')
data = databestand.read().splitlines()
round = 0
monkey = -1
monkey_inventories = []
monkey_operations = []
monkey_tests = []
for regel in range(0,len(data)):
    if regel%7 == 0:
        monkey+=1
        monkey_inventories.append([])
        monkey_operations.append([])
    if regel%7 == 1:
        items_in_monkey = ''.join(data[regel].split(' ')).split(',')
        if len(items_in_monkey[0].split('Startingitems:'))>1:
            monkey_inventories[monkey]+=[items_in_monkey[0][-2:]]
            if len(items_in_monkey)>1:
                for item in range(1,len(items_in_monkey)):
                    monkey_inventories[monkey]+=[items_in_monkey[item]]
    if regel%7 == 2:
        monkey_operations[monkey].append(data[regel][23])
        monkey_operations[monkey].append(data[regel][25:])
    if regel%7 == 3:
        monkey_tests.append([data[regel][21:]])
    if regel%7 == 4:
        monkey_tests[monkey].append(data[regel][29:])
    if regel%7 == 5:
        monkey_tests[monkey].append(data[regel][30:])
divisors = []
for test in monkey_tests:
    divisors.append(int(test[0]))
deelfactor = lcm(*divisors)

amount_of_monkeys = len(monkey_inventories)
inspections_per_monkey = [[0]*amount_of_monkeys]
inspections_per_monkey = inspections_per_monkey[0]
while round<10000:
    round+=1
    for monkey_inventory in range(0,len(monkey_inventories)):
        while len(monkey_inventories[monkey_inventory])>0:
            inspections_per_monkey[monkey_inventory]+=1
            worry_level_current_item = int(monkey_inventories[monkey_inventory][0])
            monkey_inventories[monkey_inventory].remove(str(worry_level_current_item))
            if monkey_operations[monkey_inventory][0] == '+':
                if monkey_operations[monkey_inventory][1] == 'old':
                    worry_level_current_item+=worry_level_current_item
                else:
                    worry_level_current_item+=int(monkey_operations[monkey_inventory][1])
            if monkey_operations[monkey_inventory][0] == '*':
                if monkey_operations[monkey_inventory][1] == 'old':
                    worry_level_current_item*=worry_level_current_item
                else:
                    worry_level_current_item*=int(monkey_operations[monkey_inventory][1])
            worry_level_current_item%=deelfactor
            if worry_level_current_item%int(monkey_tests[monkey_inventory][0])==0:
                monkey_inventories[int(monkey_tests[monkey_inventory][1])].append(str(worry_level_current_item))
            else:
                monkey_inventories[int(monkey_tests[monkey_inventory][2])].append(str(worry_level_current_item))
inspections_per_monkey.sort()
print(inspections_per_monkey[-1]*inspections_per_monkey[-2])






