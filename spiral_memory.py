import numpy as np

x_max = 100
y_max = 100
memory = np.zeros([x_max,y_max])
memory[x_max//2, y_max//2] = 1

puzzle_input = 361527

def dist(input):

    square = 1
    x = 0
    y = 0
    x_dir = 1
    y_dir = 1
    x_counter = 1
    y_counter = 1
    dist = 0


    while square < input:

        for _ in range(x_counter):
            x += x_dir
            square += 1
            if square == input:
                dist = abs(x) + abs(y)


        x_dir = - x_dir

        for _ in range(y_counter):
            y += y_dir
            square += 1
            if square == input:
                dist = abs(x) + abs(y)

        y_dir = - y_dir

        x_counter += 1
        y_counter += 1


    return dist

def memory_fill():

        x = 0
        y = 0
        x_dir = 1
        y_dir = 1
        x_counter = 1
        y_counter = 1

        while True:

            for _ in range(x_counter):
                x += x_dir
                memory[x_max//2+x, y_max//2+y] = neighbour_sum(x_max//2+x, y_max//2+y)
                if memory[x_max//2+x, y_max//2+y] > puzzle_input:
                    return memory[x_max//2+x, y_max//2+y]


            x_dir = - x_dir

            for _ in range(y_counter):
                y += y_dir
                memory[x_max//2+x, y_max//2+y] = neighbour_sum(x_max//2+x, y_max//2+y)
                if memory[x_max//2+x, y_max//2+y] > puzzle_input:
                    return memory[x_max//2+x, y_max//2+y]

            y_dir = - y_dir

            x_counter += 1
            y_counter += 1


def memory_update_and_check(x,y):

    memory[x_max//2+x, y_max//2+y] = neighbour_sum(x_max//2+x, y_max//2+y)
    if memory[x_max//2+x, y_max//2+y] > puzzle_input:
        return memory[x_max//2+x, y_max//2+y]

def neighbour_sum(x,y):
    return sum(memory[x+1,y-1:y+2]) + sum(memory[x-1,y-1:y+2]) + memory[x,y+1] + memory[x, y-1]
