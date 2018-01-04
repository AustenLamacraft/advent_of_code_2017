with open("inputs/stream_processing.txt") as file:
    my_stream = file.read()

def process(stream):

    accepting = True
    ignoring = False

    level = 0
    count = 0
    garbage_count = 0

    for char in stream:

        if not accepting and not ignoring and char != "!" and char != ">":
            garbage_count += 1

        if not accepting and ignoring:
            ignoring = False
        elif char == "!" and not accepting:
            ignoring = True
        elif not accepting and char == ">":
            accepting = True
        elif char == "<" and accepting:
            accepting = False
        elif char == "{" and accepting:
            level += 1
        elif char == "}" and accepting:
            count += level
            level += -1

        print("Accepting ", accepting, " Ignoring ", ignoring, " Level ", level, " Count ", count)

    return count, garbage_count
