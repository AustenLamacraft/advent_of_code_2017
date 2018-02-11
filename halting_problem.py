import numpy as np

rules = dict({})

with open("inputs/halting_problem.txt") as file:
     for line in file:

          if "In state" in line:
               state = line[-3]
               rules[state] = []

          if "current value" in line:
               current_val = int(line[-3])

          if "Write" in line:
               write = int(line[-3])

          if "Move" in line:
               if "right" in line:
                    move = 1
               else:
                    move = -1

          if "Continue" in line:
               new_state = line[-3]
               rules[state].append((write, move, new_state))

checksum = 12523873

tape_length = 1000000

tape =  np.zeros(tape_length, dtype = "bool")
state = "A"
pos = 500000

for step in range(checksum):
     if step % 100000 == 0:
          print(f"step {step}")
     write, move, new_state = rules[state][int(tape[pos])]
     tape[pos] = write
     pos += move
     state = new_state

print(sum(tape))
