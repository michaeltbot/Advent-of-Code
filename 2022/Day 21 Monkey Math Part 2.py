def speak(monkey, number, operation):
    if monkey in number:
        return number[monkey]

    m1 = speak(operation[monkey][1], number, operation)
    m2 = speak(operation[monkey][2], number, operation)

    if m1 == None or m2 == None:
        return None

    op = operation[monkey][0]

    if op == "+":
        num = m1 + m2
    elif op == "-":
        num = m1 - m2
    elif op == "*":
        num = m1 * m2
    elif op == "/":
        num = m1 / m2
    
    number[monkey] = num
    return num

def solve(monkey, equate, number, operation):
    if monkey == 'humn':
        return equate
    
    m1 = operation[monkey][1]
    m2 = operation[monkey][2]
    op = operation[monkey][0]

    if m1 not in number or number[m1] == None:
        m = m1
        num = number[m2]
        if op == "+":
            result = equate - num
        elif op == "-":
            result = equate + num
        elif op == "*":
            result = equate / num
        elif op == "/":
            result = equate * num
    else:
        m = m2
        num = number[m1]
        if op == "+":
            result = equate - num
        elif op == "-":
            result = num - equate
        elif op == "*":
            result = equate / num
        elif op == "/":
            result = num / equate
    
    return solve(m, result, number, operation)


number = dict()
operation = dict()

with open("Day 21 Monkey Math.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip("\n")

        name, value = line.split(": ")
        try:
            number[name] = int(value)
        except ValueError:
            monkey1, op, monkey2 = value.split(" ")
            operation[name] = (op, monkey1, monkey2)

operation['root'] = ("=", operation['root'][1], operation['root'][2])
number['humn'] = None

speak('root', number, operation)

m1 = operation['root'][1]
m2 = operation['root'][2]
if m1 not in number or number[m1] == None:
    result = solve(m1, number[m2], number, operation)
else:
    result = solve(m2, number[m1], number, operation)

print(result)