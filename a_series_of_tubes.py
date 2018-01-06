import numpy as np
tubes = []

with open("inputs/a_series_of_tubes.txt") as file:
    for line in file:
        tubes.append(list(line[:-1]))

tubes = np.array(tubes)

# Continue going in the same direction until we hit a +, then determine new
# direction.

row, col = 0, list(tubes[0,:]).index("|")
dir = "d"

def find_plus(row, col, dir):
    try:
        if dir == "d":
            segment = list(tubes[row+1:,col])
            end = min(segment.index("+") + 1, segment.index(" "))
            row = row + end
        elif dir == "u":
            segment = list(tubes[row-1::-1,col])
            end = min(segment.index("+") + 1, segment.index(" "))
            row = row - end  # Important to go backwards, finding first occurrence
        elif dir == "r":
            segment = list(tubes[row,col+1:])
            end = min(segment.index("+") + 1, segment.index(" "))
            col = col + end
        elif dir == "l":
            segment = list(tubes[row,col-1::-1])
            end = min(segment.index("+") + 1, segment.index(" "))
            col = col - end

        chars = [char for char in segment[:end] if char.isalpha()]
        return row, col, chars

    except ValueError:
        print("loose end at ", row, col)

def new_dir(row, col, dir):

    if tubes[row,col] != "+":
        return ""

    if dir in {"u", "d"}:
        if tubes[row, col + 1] == "-":
            dir = "r"
        else:
            dir = "l"

    elif dir in {"l","r"}:
        if tubes[row+1, col] == "|":
            dir = "d"
        else:
            dir = "u"

    return dir

def stringify(char_list):

    char_string = ""

    for char in char_list:
        char_string += char

    return char_string

char_list = []
steps = 1 # Include the first line at the top

while dir != "":
    new_row, new_col, chars = find_plus(row, col, dir)
    char_list.extend(chars)
    steps += abs(new_row - row) + abs(new_col - col)
    row, col = new_row, new_col

    dir = new_dir(row, col, dir)
    print(row, col, dir, stringify(char_list))

print("Total number of steps ", steps)
