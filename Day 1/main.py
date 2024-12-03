def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    list_a = []
    list_b = []

    for i in range (len(lines)):
        list_a.append(int(lines[i].split(' ')[0]))
        list_b.append(int(lines[i].split(' ')[-1]))

    list_a.sort()
    list_b.sort()
    
    total = 0

    for i in range(len(list_a)):
        total+= abs(list_a[i] - list_b[i])
    
    print(total)

def part2():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    list_a = []
    list_b = []
    freq = {}

    total = 0

    for i in range(len(lines)):
        list_a.append(int(lines[i].split(' ')[0]))
        list_b.append(int(lines[i].split(' ')[-1]))
        freq = dict.fromkeys(list_a, -1)
    

    keylist = list(freq.keys())

    for i in range(len(list_a)):
        if freq.get(list_a[i]) == -1:
            freq[list_a[i]] = list_b.count(list_a[i])
        total += list_a[i] * freq.get(list_a[i])

    print(total)

part2()

