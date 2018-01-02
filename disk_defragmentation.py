import binascii
import knot_hash as kh

my_string = "jzgqcdpd"

my_strings = [my_string+"-"+str(j) for j in range(128)]

hashes = [kh.knot_hash(string) for string in my_strings]

rows = [bin(int(hash,16))[2:] for hash in hashes]

# Pad them out
rows = [(128-len(row))*"0" + row for row in rows]

total_used = 0

for row in rows:
    total_used += row.count("1")

print("Total number of used squares: ", total_used)

# Make the used squares into a set

used_squares = set({})

for y, row in enumerate(rows):
    for x, square in enumerate(row):
        if square == "1":
            used_squares.add((x,y))

def find_neighbours(square):
    neighbours = {(square[0] + 1, square[1]), (square[0] - 1, square[1]), (square[0], square[1] + 1),(square[0], square[1] - 1)}
    return used_squares.intersection(neighbours)

def remove_region(first_square):

    region = {first_square}
    old_size = 0
    size = 1

    new_squares = set({})

    while size > old_size:
        old_size = size
        for square in region:
            new_squares.update(find_neighbours(square))
        region.update(new_squares)
        size = len(region)

    used_squares.difference_update(region) # Remove the region


regions = 0

while used_squares:
    remove_region(used_squares.pop())
    regions += 1

print("Number of regions: ", regions)
