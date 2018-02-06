import numpy as np

initial = []

with open("inputs/sporifica_virus.txt") as file:
    for line in file:
        initial.append(list(line[:-1]))


dirs = [np.array([-1,0]), np.array([0,1]), np.array([1,0]), np.array([0,-1])]

facing = 0

max_size = 2025
offset = 1000
pos = np.array([offset + 12,offset + 12])

grid = np.zeros((max_size, max_size), dtype = int)

for row, _ in enumerate(initial):
    for col, _ in enumerate(initial[row]):
        if initial[row][col] == "#":
            grid[offset + row, offset + col] = 2

steps = 10000000
count = 0

# Use encoding 0: clean, 1: weakened, 2: infected, 3: flagged

for j in range(steps):
    if grid[tuple(pos)] == 0:
        facing = (facing - 1) % 4
    elif grid[tuple(pos)] == 2:
        facing = (facing + 1) % 4
    elif grid[tuple(pos)] == 3:
        facing = (facing + 2) % 4

    grid[tuple(pos)] = (grid[tuple(pos)] + 1)%4
    if grid[tuple(pos)] == 2:
        count += 1

    pos += dirs[facing]

    if j % 100000 == 0:
        print(f"step {j}")

print(count)

print(grid[995:1030,995:1030])
