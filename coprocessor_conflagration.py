instructions = []

with open("inputs/coprocessor_conflagration.txt") as file:
    for line in file:
        instructions.append(line[:-1].split())

registers = {instruction[1]:0 for instruction in instructions if instruction[1].isalpha()}

registers["a"] = 1

ops = {"sub": "-=", "set": "=", "mul": "*="}

j = 0
mul_count = 0

end_count = 0

while j < len(instructions):

    instruction = instructions[j]

    cmd = instruction[0]
    x_reg = instruction[1]


    if instruction[1].isalpha():
        x_val = registers[instruction[1]]
    else:
        x_val = int(instruction[1])

    if instruction[2].isalpha():
        y_val = registers[instruction[2]]
    else:
        y_val = int(instruction[2])

    if cmd == "set":
        registers[x_reg] = y_val

    if cmd == "sub":
        registers[x_reg] -= y_val

    if cmd == "mul":
        registers[x_reg] *= y_val
        mul_count += 1


    if cmd == "jnz" and x_val != 0:
        print(f"jump at {j}!")
        j += y_val
    else:
        j += 1

    # print(f"{registers['h']} in register h")
    # print(f"{registers['g']} in register g")




print(f"{mul_count} muls")
