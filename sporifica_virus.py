import numpy as np

initial = []

with open("inputs/sporifica_virus.txt") as file:
    for line in file:
        initial.append(list(line[:-1]))


dirs = {0: np.array([-1,0]), 1: np.array([0,1]), 2: np.array([1,0]), 3: np.array([0,-1])}

facing = 0

max_size = 2025
offset = 1000
pos = np.array([offset + 12,offset + 12])

grid = np.zeros((max_size, max_size), dtype = int)

for row, _ in enumerate(initial):
    for col, _ in enumerate(initial[row]):
        if initial[row][col] == "#":
            grid[offset + row, offset + col] = 1

steps = 10000
count = 0

for _ in range(steps):
    if grid[tuple(pos)] == 1:
        facing = (facing + 1) % 4
        grid[tuple(pos)] = 0
    else:
        facing = (facing - 1) % 4
        grid[tuple(pos)] = 1
        count += 1

    pos += dirs[facing]

print(count)

print(grid[995:1030,995:1030])
