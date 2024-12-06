def is_valid(order, rules):
    for first, second in rules:
            if first not in order or second not in order:
                continue
            if order.index(first) > order.index(second):
                return False
    return True

def middle_count_calc(orders):
    middle_count = 0
    for order in orders:
        if(len(order) == 1):
            middle_count+= order[0]
        elif(len(order) == 2):
            middle_count += (order[0]+order[1])/2
        elif(len(order) % 2 == 0):
            order_1 = order[len(order)/2 - 1]
            order_2 = order[len(order)/2]
            middle_count+= (order_1 + order_2)/2
        else:
            middle_count+=order[int((len(order) - 1)/2)]
    return middle_count

def part1():
    rules = []
    orders = []
    with open("input.txt") as file:
        for line in file.readlines():
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            if ',' in line:
                orders.append(list(map(int, line.split(','))))
    print(rules)
    print(orders)

    valid_orders = []

    for order in orders:
        if is_valid(order, rules):
            valid_orders.append(order)

    print(middle_count_calc(valid_orders))  

def part2():
    rules = []
    orders = []
    with open("input.txt") as file:
        for line in file.readlines():
            if '|' in line:
                rules.append(tuple(map(int, line.split('|'))))
            if ',' in line:
                orders.append(list(map(int, line.split(','))))

    invalid_orders = []

    for order in orders:
        if not is_valid(order, rules):
            invalid_orders.append(order)
    
    for invalid_order in invalid_orders:
        while not is_valid(invalid_order, rules):
            for first, second in rules:
                if first not in invalid_order or second not in invalid_order:
                    continue
                first_index = invalid_order.index(first)
                second_index = invalid_order.index(second)
                if first_index > second_index:
                    invalid_order[first_index] = second
                    invalid_order[second_index] = first

    print(middle_count_calc(invalid_orders))

part2()