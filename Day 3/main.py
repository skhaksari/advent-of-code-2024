import re 

def part1():
    program_memory = ''

    with open("input.txt") as file:
        program_memory = file.read()

    print(program_memory)

    operations = re.findall( r'mul\([0-9]+,[0-9]+\)', program_memory)

    total = 0

    for operation in operations:
        nums = operation[4:len(operation) - 1]
        num_split = nums.split(",")
        total += int(num_split[0]) * int(num_split[1])

    print(total)

def part2():
   
    program_memory = ''

    patterns = [
    r"mul\([0-9]+,[0-9]+\)",  # Pattern for mul operation
    r"do\(\)",  # Do operation pattern
    r"don't\(\)" #Don't operation pattern
    ]

    combined_pattern = "|".join(patterns)

    with open("input.txt") as file:
        program_memory = file.read()

    print(program_memory)

    operations = re.findall(combined_pattern, program_memory)

    print(operations)

    total = 0

    operation_disabled = False

    for operation in operations:
        if operation == "do()":
            operation_disabled = False
        elif operation == "don't()":
            operation_disabled = True
        if not operation_disabled and operation[:4] == "mul(":
            nums = operation[4:len(operation) - 1]
            num_split = nums.split(",")
            total += int(num_split[0]) * int(num_split[1])

    print(total) 
    
part2()