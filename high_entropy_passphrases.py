total = 0
valid_passphrases = 0

with open("passphrases.txt") as file:
    for line in file:
        line_list = line.split()
        if len(set(line_list)) == len(line_list):
            total += 1

        # Second part...
        word_letters = {tuple(sorted(word)) for word in line_list}
        if len(word_letters) == len(line_list):
            valid_passphrases += 1


    print(total, valid_passphrases)
