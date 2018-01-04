with open("inputs/twisty_trampolines.txt") as file:
    input_strings = file.read().split("\n")
    input = [int(line) for line in input_strings[:-1]]

    pos = 0
    step = 1
    while True:
        jump = input[pos]
        new_pos = pos + jump
        if input[pos] > 2:
            input[pos] -= 1
        else:
            input[pos] += 1

        if new_pos  >= len(input) or new_pos <0:
            break

        pos = new_pos
        step += 1

    print(step)
