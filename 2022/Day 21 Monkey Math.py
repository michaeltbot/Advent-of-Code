def speak(monkey, number, operation):
    if monkey in number:
        return number[monkey]

    m1 = speak(operation[monkey][1], number, operation)
    m2 = speak(operation[monkey][2], number, operation)
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

print(speak('root', number, operation))

