instructions = []

with open("inputs/duet.txt") as file:
    for line in file:
        instructions.append(line[:-1].split())

registers = {instruction[1]:[0,0] for instruction in instructions if instruction[1].isalpha()}

ops = {"add": "+=", "set": "=", "mul": "*="}

registers["p"] = [0,1]
q = [[],[]] # This is the queue
dead_lock = [False, False]
indices = [0,0]
send_count = [0,0]

while dead_lock != [True, True]:

    try:
        cmds = (instructions[indices[0]], instructions[indices[1]])

        for prog, cmd in enumerate(cmds):
            if cmd[1].isalpha():
                var = "registers[cmd[1]][prog]"
            else:
                var = cmd[1]

            if len(cmd) == 3:
                if cmd[2].isalpha():
                    val = "registers[cmd[2]][prog]"
                else:
                    val = cmd[2]

            if cmd[0] in ops.keys():
                exec(var + ops[cmd[0]] + val)
            if cmd[0] == "mod":
                exec(var + "=" + var + "%" + val)
            if cmd[0] == "snd":
                q[not prog].append(eval(var)) # Add to the other queue
                send_count[prog] += 1
                print(q)
            if cmd[0] == "jgz" and eval(var) > 0:
                indices[prog] += eval(val)
            elif cmd[0] == "rcv":
                try:
                    registers[cmd[1]][prog] = q[prog].pop(0)
                    indices[prog] += 1
                    dead_lock[prog] = False
                except IndexError:
                    dead_lock[prog] = True

            else:
                indices[prog] += 1


    except IndexError:
        dead_lock = [True, True]
