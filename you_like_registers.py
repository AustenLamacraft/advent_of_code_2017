import re

instructions = []
conditions = []

with open("you_like_registers.txt") as file:
    for line in file:
        instruction, condition = line.split("if")
        instructions.append(instruction.split())
        conditions.append(condition.strip())

# Initialize values
for entry in instructions:
    exec(entry[0]+"=0")

max_values = []

for index, line in enumerate(instructions):
    if eval(conditions[index]):
        if line[1] == "inc":
            exec(line[0]+"+="+line[2])
        elif line[1] == "dec":
            exec(line[0]+"-="+line[2])

    max_values.append(max([eval(entry[0]) for entry in instructions]))

registers = {entry[0] : eval(entry[0]) for entry in instructions}

print(max(registers.values()))
print("Largest value during whole run: ",max(max_values))
