import numpy as np
from sympy.combinatorics import Permutation

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

def stringify(prog_list):

    prog_string = ""

    for prog in prog_list:
        prog_string += prog

    return prog_string

print(stringify(programs))

# The second part is sufficiently sneaky that it's worth paying homage to.
# Point is that the we DO NOT simply take the billionth power of the permutation
# from the previous part. The "partner" move swaps named programs NO MATTER WHERE
# they are! Thus doing the whole sequence a billion (or any even number) of times
# renders all the partner moves void. Comment them out and THEN take the billionth
# power!

# I did the permutations by hand before and it was slow. SymPy does it in a jiffy.

# Here's the permutation corresponding to the output pkgnhomelfdibjac from the first part
abcd = "abcdefghijklmnop"
one_dance = [abcd.index(char) for char in programs]

perm = Permutation(one_dance)

final_perm = perm**1000000000

print(stringify([abcd[val] for val in final_perm]))
