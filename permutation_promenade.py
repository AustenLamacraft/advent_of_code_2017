import numpy as np

with open("permutation_promenade.txt") as file:
    moves = file.read()[:-1].split(",")

class DanceMoves(list):

    def spin(self, cycle):
        np_progs = np.array(self)
        np_progs = np.roll(np_progs, cycle)
        self[:] = np_progs

    def exchange(self, a, b):
        self[a], self[b] = self[b], self[a]

    def partner(self, a, b):
        a_index = self.index(a)
        b_index = self.index(b)
        self[a_index], self[b_index] = self[b_index], self[a_index]
        # self[self.index(a)], self[self.index(b)] = self[self.index(b)], self[self.index(a)]
        # The commented line doesn't work... why?

programs = DanceMoves(list("abcdefghijklmnop"))

for move in moves:
    if move[0] == "s":
        programs.spin(int(move[1:]))
    elif move[0] == "x":
        a, b = move[1:].split("/")
        programs.exchange(int(a), int(b))
    elif move[0] == "p":
        a, b = move[1:].split("/")
        programs.partner(a, b)

prog_string = ""

for prog in programs:
    prog_string += prog

print(prog_string)
