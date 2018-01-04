import numpy as np

with open("inputs/memory_reallocation.txt") as file:
    input_strings = file.read().split("\t")
    block_counts = [int(count) for count in input_strings]

def reallocate(block_counts):
    biggest, num_blocks = np.argmax(block_counts), np.max(block_counts)
    block_counts[biggest] = 0

    for shift in np.arange(1, num_blocks + 1):
        block_counts[(biggest + shift) % 16] += 1

    return block_counts

block_count_record = [tuple(block_counts)]

count = 1

while True:

    block_counts = reallocate(block_counts)
    block_count_record.append(tuple(block_counts))

    if len(set(block_count_record)) != len(block_count_record):
        break

    count += 1

print(count)
print(count - block_count_record.index(tuple(block_counts)))
