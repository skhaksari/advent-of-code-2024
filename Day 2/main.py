def is_safe(numbers):
    
    for i in range(len(numbers)-1):
        a, b = numbers[i], numbers[i+1]
        if not 1 <= abs(a - b) <= 3:
            return False
        
        if i >= len(numbers) - 2:
            continue

        c = numbers[i+2]

        if not a < b < c and not a > b > c:
            return False
        
    return True

def part2():
    reports = []
    
    with open("input.txt") as file:
        reports = file.readlines()

    safe_count = 0
    
    for report in reports:
        numbers = list(map(int, report.split(' ')))
                      
        if(is_safe(numbers)):
            safe_count += 1
        else: 
            for i in range (len(numbers)):
                numbers_slice = numbers[:i] + numbers[i+1:]
                if(is_safe(numbers_slice)):
                    safe_count += 1
                    break

    
    print(safe_count)

def part1():
    reports = []
    
    with open("input.txt") as file:
        reports = file.readlines()

    safe_count = 0
    
    for report in reports:
        numbers = list(map(int, report.split(' ')))
                      
        if(is_safe(numbers)):
            safe_count += 1
    
    print(safe_count)

part1()
part2()
    