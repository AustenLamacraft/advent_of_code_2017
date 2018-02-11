import numpy as np

rules = {}

def io_parse(grid):
    grid = grid.strip()
    grid = grid.split("/")
    return tuple([tuple(line) for line in grid])

with open("inputs/fractal_art.txt") as file:
    for line in file:
        input, output = line.split("=>")
        input = io_parse(input)
        output = io_parse(output)
        rules[input] = output

def quarter_turn(grid):
    return grid.T[:,::-1]

def variants(grid):
    "Generate the set of 8 symmetry related grids"
    variants = []

    for _ in range(2):
        for _ in range(4):
            variants.append(grid)
            grid = quarter_turn(grid)
        grid = grid[:,::-1] # Reflect in the vertical

    return variants

# Make all variants of the rule inputs upfront
# My original solution calculated the variants for each subgrid arising -- much slower
rule_variants = {}

for key in rules.keys():
    rule_variants[key] = variants(np.array(key))

def input_match(grid):
    "return rule input matching square"
    grid = np.array(grid)
    matches = []
    for key in rules.keys():
        if any([np.array_equal(grid, variant) for variant in rule_variants[key]]):
            matches.append(key)
    return matches[0]

def make_subgrids(grid):
    "Split a grid into subgrids"
    grid = np.array(grid)

    if len(grid) % 2 == 0:
        block  = 2
    else:
        block = 3
    return [[grid[block*j:block*(j+1),block*k:block*(k+1)] for k in range(len(grid) // block)] for j in range(len(grid) // block)]

def make_grid(subgrids):
    "Form subgrids into a grid"
    size = len(subgrids)
    return np.concatenate([np.concatenate([subgrids[i][j] for j in range(size)],axis=1) for i in range(size)], axis=0)

def apply_rules(grid):
    subgrids = make_subgrids(grid)
    size = len(subgrids)
    for i in range(size):
        for j in range(size):
            subgrids[i][j] = rules[input_match(subgrids[i][j])]
    return make_grid(subgrids)


grid = np.array([[".","#", "."],[".", ".", "#"],["#","#","#"]])

for j in range(18):
    print(f"calculating {j}th iteration")
    grid = apply_rules(grid)
    print(f"grid is size {len(grid)} after {j}th iteration")

pixels_on = np.sum(grid == "#")
print(f"Number of pixels on: {pixels_on}")
