
checksum = 0
ratios = 0

with open("corruption_checksum.txt") as file:
    for line in file:
        numbers = [int(entry) for entry in line[:-1].split("\t")]
        checksum += max(numbers) - min(numbers)

        ratios += sum([ i / j for i in numbers for j in numbers if i % j == 0]) - len(numbers)

print(checksum, ratios)
