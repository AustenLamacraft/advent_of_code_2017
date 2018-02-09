from collections import Counter
components = []

with open("inputs/electromagnetic_moat.txt") as file:
    for line in file:
        components.append([int(port) for port in line[:-1].split("/")])

entries = []
for component in components:
    entries += component

port_count = Counter(entries)

endports = {(port, port) for port in port_count if port_count[port] == 1}

allports = {(port, port) for port in entries}

scores = []

def find_path(endport, remaining_components, path) :
    if endport[0] != 0:
        for component in remaining_components:
            if endport[0] in component:
                next_port = component[int(not component.index(endport[0]))]
                score = endport[1] + 2*next_port
                new_components = remaining_components[:]
                new_components.remove(component)
                find_path((next_port,score),new_components, path + [next_port])
    else:
        scores.append(endport[1])

for port in endports:
    find_path(port, components, [port[0]])
