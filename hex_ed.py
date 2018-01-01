import numpy as np

# Convert triangular lattice to square lattice with a diagonal
n, ne, se, s, sw, nw = np.array([0,1]), np.array([1,0]), np.array([1,-1]), np.array([0,-1]), np.array([-1,0]), np.array([-1,1])

directions = {"n": n, "ne": ne, "se": se, "s": s, "sw": sw, "nw": nw}

with open("hex_ed.txt") as file:
    my_path = file.read()[:-1].split(",")

def hex_distance(path):

    disp = sum([directions[step] for step in path])

    if disp[0] * disp[1] >= 0:
        return abs(disp[0]) + abs(disp[1])
    else:
        return min(abs(disp)) + max(abs(disp)) - min(abs(disp))

all_disp = []

for index, _ in enumerate(my_path):
    all_disp.append(hex_distance(my_path[:index+1]))

print(max(all_disp))
